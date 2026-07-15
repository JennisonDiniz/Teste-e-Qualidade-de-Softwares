import time

def rodar_laboratorio():
    tamanho_giga = 15000
    tempo_inicial = time.time()

    # Simulando uma busca ineficiente de dados (O(N^2))
    resultado = []
    for i in range(tamanho_giga):
        for j in range(tamanho_giga):#comentar essa linha para melhorar a performance
            if i == j:#comentar essa linha para melhorar a performance
                resultado.append(i)

    tempo_final = time.time()
    tempo_execucao = tempo_final - tempo_inicial
    
    print(f"Tempo de Execução: {tempo_execucao:.4f} segundos")
    print("Total de itens processados:", len(resultado))

rodar_laboratorio()
