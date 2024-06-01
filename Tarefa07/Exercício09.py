# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python e laço de repetição While

# Elaborar um programa que efetue a leitura de valores positivos inteiros até que
# um valor negativo seja informado. Ao final devem ser apresentados o maior e o menor
# valores informados pelo usuário.

numero = 1
maior = 0
menor = 0
temporaria = 0

while numero >= 0:
    temporaria = float(input("Insira um número: "))
    if temporaria > maior:
        maior = temporaria
        numero = temporaria
    elif temporaria < menor:
        menor = temporaria
        numero = temporaria
    else:
        numero = temporaria

print("O maior número é",maior,"E o menor número é",menor)
