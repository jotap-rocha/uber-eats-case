import pytest


@pytest.fixture(autouse=True)
def gcp_test_environment(monkeypatch):
    """Variáveis dummy para o código nunca tentar resolver credenciais GCP reais."""
    monkeypatch.setenv("GCP_PROJECT_ID", "test-project")
    monkeypatch.setenv("GOOGLE_APPLICATION_CREDENTIALS", "")
