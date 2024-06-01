# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python e laço de repetição While

# Elaborar um programa que efetue a leitura de 10 valores numéricos e apresente no
# final o total do somatório e a média aritmética dos valores lidos.


soma = 0
range = 1
while range < 11:
    valor = float(input("Insira um valor qualquer:"))
    soma += valor
    range += 1
print("A soma dos valores é", soma, "Enquanto sua média aritmética é", soma/10)