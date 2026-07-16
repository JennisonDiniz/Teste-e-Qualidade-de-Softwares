import pytest
from unittest.mock import patch
from loja import finalizar_compra

# Desafio 1: Testar o caminho de Sucesso garantindo que o e-mail foi enviado
@patch('loja.enviar_email_confirmacao')
def test_deve_finalizar_compra_e_enviar_email(mock_enviar_email):
    # 1. Configuração do cenário
    saldo = 100.0
    valor_compra = 80.0
    email = "cliente@exemplo.com"
    
    # 2. Execução da ação
    resultado = finalizar_compra(saldo, valor_compra, email)
    
    # 3. Asserção do comportamento do sistema
    assert resultado == "Sucesso: Compra finalizada"
    
    # Verificação do Mock: Garante que o e-mail foi enviado exatamente uma vez com os dados corretos
    mock_enviar_email.assert_called_once_with(email, valor_compra)


# Desafio 2: Testar o caminho de Erro garantindo que o e-mail NÃO foi enviado
@patch('loja.enviar_email_confirmacao')
def test_nao_deve_enviar_email_se_saldo_insuficiente(mock_enviar_email):
    # 1. Configuração do cenário (Compra maior que o saldo)
    saldo = 50.0
    valor_compra = 120.0
    email = "cliente@exemplo.com"
    
    # 2. Execução da ação
    resultado = finalizar_compra(saldo, valor_compra, email)
    
    # 3. Asserção do comportamento do sistema
    assert resultado == "Erro: Saldo insuficiente"
    
    # Verificação do Mock: Garante que a função de e-mail NUNCA foi acionada
    mock_enviar_email.assert_not_called()