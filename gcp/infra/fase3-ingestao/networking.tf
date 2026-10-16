# Rede da Fase 3 — só hospeda o bastion (Decisão 1 do DESIGN). A Fase 0 continua
# rodando localmente; não há VPC "espelhando a Fase 0" como na AWS (Decisão 1
# da Fase 2, rejeitada aqui como Abordagem D no brainstorm).

resource "google_compute_network" "fase3" {
  name                    = "${var.project_prefix}-vpc"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "bastion" {
  name          = "${var.project_prefix}-bastion-subnet"
  ip_cidr_range = var.vpc_cidr
  region        = var.gcp_region
  network       = google_compute_network.fase3.id
}

# SSH administrativo (operador humano) — nunca 0.0.0.0/0
resource "google_compute_firewall" "bastion_ssh_admin" {
  name          = "${var.project_prefix}-bastion-ssh-admin"
  network       = google_compute_network.fase3.id
  direction     = "INGRESS"
  source_ranges = [var.admin_access_cidr]

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  target_tags = ["bastion"]
}

# SSH do Datastream, via Forward SSH tunnel connectivity profile (Decisão 1).
# Ver nota em variables.tf sobre datastream_source_ranges não ter um bloco fixo
# publicado — confirmar e restringir no /build antes do apply real.
resource "google_compute_firewall" "bastion_ssh_datastream" {
  name          = "${var.project_prefix}-bastion-ssh-datastream"
  network       = google_compute_network.fase3.id
  direction     = "INGRESS"
  source_ranges = var.datastream_source_ranges

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  target_tags = ["bastion"]
}
