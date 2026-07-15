def verificar_idade(idade):
    if idade >= 18:
        return "Acesso Permitido"
    else:
        return "Acesso Negado"
        
    # Esta linha deveria salvar um log de segurança no terminal.
    # Por que ela nunca é executada pelo programa?
print("LOG DE SEGURANÇA: Verificação de idade concluída com sucesso no sistema!")# Agora a mensagem de log é impressa ANTES de encerrarmos a função

# --- ÁREA DE TESTE ---
# Você pode executar este arquivo para ver o que ele imprime na tela.
resultado = verificar_idade(20)
print("Resultado do sistema:", resultado)

#3. Respostas para o seu caderno/anotações Onde está o "Código Morto"? O código morto está na linha 10 do arquivo login.py:Por que essa linha nunca é executada? Essa linha nunca é executada porque ela foi escrita depois da instrução return em ambos os fluxos da estrutura condicional (if e else). A instrução return tem duas funções principais em uma função: Devolver um valor para quem chamou a função. Encerrar imediatamente a execução da função. Assim que o Python encontra qualquer um dos return, ele sai da função verificar_idade na hora e ignora completamente qualquer linha de código que venha abaixo deles dentro daquele mesmo bloco.