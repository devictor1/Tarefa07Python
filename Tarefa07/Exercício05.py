# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python e laço de repetição While

# Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit,
# de 10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius.
# O programa deve apresentar os valores das duas temperaturas. A fórmula de conversão é
# F = 9C+160/5, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

celsius = 10
while celsius < 101:
    fahrenheit = (9*celsius+160)/5
    print("A temperatura, em celsius, é", celsius, "E, em Fahrenheit,", fahrenheit)
    celsius += 10