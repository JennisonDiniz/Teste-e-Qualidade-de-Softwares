def calcular_frete(valor_compra):
    # REGRA DE NEGÓCIO: Frete grátis para compras de R$ 100,00 ou mais.
    if valor_compra >= 100: # CORREÇÃO: Alterado de '>' para '>=' para incluir o valor limite de 100.
        return "Frete Grátis"
    else:
        return "Frete: R$ 20,00"

# ============ ÁREA DE TESTE ============
# Você pode executar este arquivo para ver o que ele imprime na tela.
print("Testando compra de R$ 150,00:", calcular_frete(150)) # Esperado: Frete Grátis
print("Testando compra de R$ 50,00 :", calcular_frete(50))  # Esperado: Frete R$ 20
print("Testando compra de R$ 100,00:", calcular_frete(100)) # Esperado: Frete Grátis

#1.O Erro (Ação Humana)O que aconteceu: O desenvolvedor interpretou incorretamente a regra de negócio. Ao ler "compras de R$ 100,00 ou mais", ele desconsiderou o valor exato de limite (R$ 100,00) e pensou apenas em valores estritamente maiores que 100 (> 100).
#2. O Defeito (Bug no Código) Onde está: Na linha 3 do arquivo.O que está incorreto: O operador de comparação utilizado foi o de "maior que" (>). Para incluir o valor de R$ 100,00, o correto seria utilizar o operador de "maior ou igual a" (>=).
#3. A Falha (Comportamento Visível)O que o cliente vê: Ao tentar finalizar uma compra de exatamente R$ 100,00, o sistema cobra o frete de R$ 20,00 na tela, quando na verdade o cliente deveria receber o benefício do Frete Grátis.