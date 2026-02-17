# Função que busca um valor na matriz e retorna as posições
def buscar_em_matriz(matriz, valor):
    posicoes = []  # Lista para guardar as posições encontradas

    for i in range(len(matriz)):         # percorre as linhas
        for j in range(len(matriz[i])):  # percorre as colunas
            if matriz[i][j] == valor:
                posicoes.append((i, j))  # salva a posição 

    if posicoes:
        return f"O valor {valor} foi encontrado nas posições: {posicoes}"
    else:
        return f"O valor {valor} NÃO foi encontrado na matriz."

# Programa principal
matriz_exemplo = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

x = int(input("Digite o valor que deseja buscar na matriz: "))
mensagem = buscar_em_matriz(matriz_exemplo, x)
print(mensagem)
