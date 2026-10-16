"""Consumidor do Kappa (Decisão 6, DESIGN_INGESTAO_GCP_FASE3.md).

Lê eventos do Pub/Sub e enriquece eventos de Pedido com o "Perfil de
Restaurante" (menu + horários), lido da cópia estática do MongoDB já
materializada como tabela Iceberg do BigLake pelo trilho batch (Etapa 2) -
o MongoDB nunca entra pelo Pub/Sub (decisão do DEFINE/brainstorm).
"""
from __future__ import annotations

import json

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from mongo_lookup import load_restaurant_profiles


class EnrichWithRestaurantProfile(beam.DoFn):
    """Enriquece o payload decodificado com o perfil do restaurante, se conhecido."""

    def process(self, element: bytes, profiles: dict):
        payload = json.loads(element)
        restaurant_id = payload.get("restaurant_id")
        if restaurant_id is not None and restaurant_id in profiles:
            payload["restaurant_profile"] = profiles[restaurant_id]
        yield payload


def run(pipeline_args: list[str], input_subscription: str) -> None:
    options = PipelineOptions(pipeline_args, streaming=True)
    with beam.Pipeline(options=options) as pipeline:
        # Side input recarregado a cada janela fixa (5 min) - mesmo papel do
        # cache-com-TTL da Lambda consumidora na AWS (Decisão 6).
        profiles_side_input = (
            pipeline
            | "PeriodicImpulse" >> beam.transforms.periodicsequence.PeriodicImpulse(
                fire_interval=300
            )
            | "LoadProfiles" >> beam.Map(lambda _: load_restaurant_profiles())
        )

        (
            pipeline
            | "ReadFromPubSub" >> beam.io.ReadFromPubSub(subscription=input_subscription)
            | "Enrich" >> beam.ParDo(
                EnrichWithRestaurantProfile(),
                profiles=beam.pvalue.AsSingleton(profiles_side_input),
            )
            # Destino final (novo tópico, BigQuery streaming insert, log
            # estruturado) - detalhar no /build seguinte, quando o formato de
            # consumo downstream do Kappa for definido (mesma pendência já
            # registrada na Fase 2/AWS).
        )


if __name__ == "__main__":
    import sys

    run(pipeline_args=sys.argv[2:], input_subscription=sys.argv[1])
