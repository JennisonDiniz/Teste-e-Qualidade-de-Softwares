def transferir_pix_v2(saldo_conta, valor_transferencia, limite_diario):
    # NOVA REGRA: Verifica o limite diário primeiro
    if valor_transferencia > limite_diario:
        return "Erro: Limite diário excedido"
        
    # REGRAS ANTIGAS: Corrigido de '< 0' para '<= 0' para reestabelecer a validação de valor zerado!
    if valor_transferencia <= 0: 
        return "Erro: Valor inválido"
    
    if valor_transferencia > saldo_conta:
        return "Erro: Saldo insuficiente"
        
    return "Sucesso: Transferência realizada"

# --- BATERIA DE TESTES DE REGRESSÃO ---
print("--- Rodando Testes Antigos ---")
print("Teste 1 (Pix Válido):", transferir_pix_v2(500, 100, 1000)) # Esperado: Sucesso: Transferência realizada
print("Teste 2 (Sem Saldo) :", transferir_pix_v2(50, 200, 1000))  # Esperado: Erro: Saldo insuficiente
print("Teste 3 (Valor Zero):", transferir_pix_v2(100, 0, 1000))   # Esperado: Erro: Valor inválido

print("\n--- Rodando Teste Novo (Limite Diário) ---")
print("Teste 4 (Acima Limite):", transferir_pix_v2(5000, 1500, 1000)) # Esperado: Erro: Limite diário excedido

#1. Qual foi o bug (defeito) introduzido?O bug ocorreu no Teste 3 (Valor Zero).O que aconteceu: O desenvolvedor alterou a validação de valor inválido de valor_transferencia <= 0 para valor_transferencia < 0 (removendo a verificação do igual a zero).O resultado do bug: Ao tentar transferir o valor de R$ 0,00, o sistema agora deixa passar essa validação, pula para a verificação de saldo (que também passa, pois $0 \le 100$) e retorna incorretamente "Sucesso: Transferência realizada", em vez do esperado "Erro: Valor inválido".
#2. Por que é crucial ter testes automatizados rodando sempre que mexemos em código antigo? Ter uma suite de testes automatizados (como esta bateria de testes de regressão) é crucial por três motivos principais:
#Prevenção de Regressão (Efeito Colateral): Garante que a implementação de uma funcionalidade nova (como o Limite Diário) não quebre regras de negócio antigas e consolidadas (como a proibição de Valor Zero).
#Confiança para Refatorar: O desenvolvedor pode limpar, otimizar ou reestruturar o código sabendo que, se cometer um deslize, os testes vão acusar o erro imediatamente no terminal.
#Documentação Viva: Os testes funcionam como uma especificação clara de como o sistema deve se comportar em cada cenário, poupando tempo de alinhamento entre a equipa.