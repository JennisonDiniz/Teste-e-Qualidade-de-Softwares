import pytest
from unittest.mock import patch
from calculadora_nuvem import calcular_desconto_por_cpf

# ❌ Teste antigo (Demorado e arriscado)
def test_desconto_sem_mock():
    resultado = calcular_desconto_por_cpf(100, "12345678900")
    assert resultado == 20.0

# ✅ Teste Corrigido com Mock/Stub (Super veloz e isolado)
@patch('calculadora_nuvem.consultar_tipo_cliente_na_api')
def test_desconto_com_mock(mock_api):
    # 1. Configuramos o comportamento do nosso Dublê (Stub)
    mock_api.return_value = "VIP"
    
    # 2. Executamos a função. Ela vai achar que chamou a API, mas chamou o mock!
    resultado = calcular_desconto_por_cpf(100, "12345678900")
    
    # 3. Validamos se o cálculo de desconto para VIP funcionou
    assert resultado == 20.0
    
    # 4. Boa prática extra: Garante que a API fictícia foi chamada exatamente uma vez
    mock_api.assert_called_once_with("12345678900")