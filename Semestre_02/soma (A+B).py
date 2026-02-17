# Entrar com valores inteiros para uma matriz A4x4 e para uma matriz B4x4. Gerar e
# imprimir a SOMA (A+B).

# Inicializa as matrizes A e B
A = []
B = []
SOMA = []

print("Digite os elementos da matriz A (4x4):")
for i in range(4):
    linha_A = []
    for j in range(4):
        valor = int(input("A[" + str(i) + "][" + str(j) + "]: "))
        linha_A.append(valor)
    A.append(linha_A)

print("\nDigite os elementos da matriz B (4x4):")
for i in range(4):
    linha_B = []
    for j in range(4):
        valor = int(input("B[" + str(i) + "][" + str(j) + "]: "))
        linha_B.append(valor)
    B.append(linha_B)

# Calcula a soma das matrizes A + B
for i in range(4):
    linha_soma = []
    for j in range(4):
        soma = A[i][j] + B[i][j]
        linha_soma.append(soma)
    SOMA.append(linha_soma)

# Exibe a matriz resultante da soma
print("\nMatriz SOMA (A + B):")
for i in range(4):
    print(SOMA[i])

#    print(SOMA[i][0], SOMA[i][1], SOMA[i][2], SOMA[i][3])
