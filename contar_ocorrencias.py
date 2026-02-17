# Função que conta quantas vezes uma palavra aparece na lista
def contar_ocorrencias(lista, palavra):
    contador = 0
    for item in lista:
        if item == palavra:
            contador += 1
    return f"A palavra '{palavra}' aparece {contador} vez(es) na lista."

# Programa principal
palavras = ["carro", "ônibus", "trem", "avião", "bicicleta", "trator",
            "carro", "ônibus", "trem", "navio", "foguete", "carroça",
            "navio", "foguete", "carroça", "carro", "trem", "trator"]

x = input("Digite a palavra que deseja buscar: ")
mensagem = contar_ocorrencias(palavras, x)
print(mensagem)

