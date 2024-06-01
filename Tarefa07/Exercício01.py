# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python e laço de repetição While

# Apresentar os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.

numero = float(input("Digite um número qualquer"))
multiplicadora = 1
while multiplicadora < 11 :
    numeroMultiplicado = numero * multiplicadora
    print("Seu número multiplicado por",multiplicadora," fica",numeroMultiplicado)
    multiplicadora+=1