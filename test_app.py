import pytest
from app import app # Importa a nossa aplicação 'app' do arquivo app.py

@pytest.fixture()
def client():
    # Cria um cliente de teste, um "navegador de mentira" para nossa aplicação
    return app.test_client()

def test_home_page(client):
    """
    Esta função testa a nossa página inicial.
    """
    # 1. Simula uma visita à página principal ("/")
    response = client.get("/")

    # 2. Verifica se a página respondeu com sucesso (código 200 = OK)
    assert response.status_code == 200

    # 3. Verifica se o conteúdo da página contém nossa mensagem de boas-vindas
    assert b"Bem-vindo ao nosso projeto" in response.data