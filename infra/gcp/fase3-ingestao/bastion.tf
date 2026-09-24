# Bastion GCE mínimo (Decisão 1, DESIGN_INGESTAO_GCP_FASE3.md) — só encaminha o
# túnel SSH reverso partindo da máquina local; não roda o docker-compose.yml da
# Fase 0 (diferente da EC2 da Fase 2/AWS).

resource "google_compute_instance" "bastion" {
  name         = "${var.project_prefix}-bastion"
  machine_type = var.bastion_machine_type
  zone         = var.gcp_zone
  tags         = ["bastion"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
      size  = 10
    }
  }

  network_interface {
    network    = google_compute_network.fase3.id
    subnetwork = google_compute_subnetwork.bastion.id

    access_config {
      # IP público — necessário para o Datastream (fora da VPC) alcançar o
      # bastion via SSH (Forward SSH tunnel connectivity profile).
    }
  }

  metadata = {
    ssh-keys = "tunnel-user:${var.bastion_ssh_public_key}"
  }

  # Nenhum outro serviço roda aqui — o bastion só existe para encaminhar o
  # túnel reverso que a máquina local abre (ver deploy/autossh/ e
  # docs/gcp/bastion-ssh-tunnel-setup.md).
}

output "bastion_public_ip" {
  description = "IP público do bastion — usado no `autossh` local e na connectivity profile do Datastream"
  value       = google_compute_instance.bastion.network_interface[0].access_config[0].nat_ip
}
