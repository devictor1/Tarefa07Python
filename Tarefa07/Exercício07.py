# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python e laço de repetição While

# Elaborar um programa que apresente os resultados da soma e da média
# aritmética dos valores pares situados na faixa numérica de 50 a 70.

contadora = 0
soma = 0
range = 50
while range < 71:
    if range % 2 == 0:
        soma += range
        contadora += 1
    range += 1
print("A soma dos valores é",soma,"E a média aritmética é", soma/contadora)