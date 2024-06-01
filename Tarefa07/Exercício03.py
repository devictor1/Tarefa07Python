# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python e laço de repetição While

# Elaborar um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.

contadora = 1
soma = 0
while contadora <501:
    if contadora % 2 == 0:
        soma += contadora
    contadora += 1
print(soma)