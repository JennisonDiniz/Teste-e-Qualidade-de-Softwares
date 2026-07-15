def transferir_pix(saldo_conta, valor_transferencia):
    # Caminho lógico 1: Validação de valor nulo ou negativo
    if valor_transferencia <= 0:
        return "Erro: Valor inválido"
    
    # Caminho lógico 2: Validação de saldo
    if valor_transferencia > saldo_conta:
        return "Erro: Saldo insuficiente"
        
    # Caminho lógico 3: Sucesso
    saldo_conta = saldo_conta - valor_transferencia
    return "Sucesso: Transferência realizada"

# --- ÁREA DE TESTE (CAIXA BRANCA) ---
# O seu objetivo é garantir que o sistema passa por todos os 'return' acima.
# Escreva abaixo os seus testes (um exemplo já está feito):

# Exemplo: Forçando o Caminho 1 (Valor inválido)
print("Teste Caminho 1:", transferir_pix(saldo_conta=100, valor_transferencia=0))

# Forçando o Caminho 2 (Saldo insuficiente)
# O valor é positivo, mas é maior que o saldo em conta.
print("Teste Caminho 2:", transferir_pix(saldo_conta=50, valor_transferencia=100))

# Forçando o Caminho 3 (Sucesso)
# O valor é positivo e menor ou igual ao saldo disponível.
print("Teste Caminho 3:", transferir_pix(saldo_conta=200, valor_transferencia=150))


#Parte A: Teste de Caixa Preta (Olhando de Fora)Como não especificou as regras de negócio exatas no seu texto, deduzimos o comportamento esperado com base no funcionamento padrão de uma transferência bancária (não transferir valores negativos/nulos e não gastar o que não tem).
#Parte B: Teste de Caixa Branca (Olhando de Dentro)1 & 2. Análise de Caminhos LógicosAnalisando a estrutura da função transferir_pix em pix.py, existem exatamente 3 caminhos lógicos (ou ramos de execução) que o sistema pode tomar, cada um terminando em um ponto de retorno (return) diferente:
#Caminho 1: Ocorre quando valor_transferencia <= 0. O fluxo entra no primeiro if e retorna "Erro: Valor inválido".
#Caminho 2: Ocorre quando o valor é positivo, mas valor_transferencia > saldo_conta. O fluxo passa pelo primeiro if, entra no segundo e retorna "Erro: Saldo insuficiente".
#Caminho 3: Ocorre quando o valor é positivo e há saldo suficiente. O fluxo ignora ambos os if, calcula o novo saldo e retorna "Sucesso: Transferência realizada".