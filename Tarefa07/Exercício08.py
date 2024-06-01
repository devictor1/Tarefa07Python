# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python e laço de repetição While

# Elaborar um programa que possibilite calcular a área total de uma residência (sala, cozinha,
# banheiro, quartos, área de serviço, quintal, garagem, etc.). O programa deve solicitar a
# entrada do nome, a largura e o comprimento de um determinado cômodo. Em seguida, deve apresentar
# a área do cômodo lido e também uma mensagem solicitando do usuário a confirmação de continuar
# calculando novos cômodos. Caso o usuário responda “NAO”, o programa deve apresentar o valor total
# acumulado da área residencial.

queroContinuar = True
areaTotal = 0

while queroContinuar is True:
    nomeComodo = input("De qual cômodo você deseja calcular a área? ")
    larguraComodo = float(input("Digite a largura de um dos comodos escolhidos "))
    comprimentoComodo = float(input("Agora, digite o comprimento desse cômodo "))
    areaComodo = larguraComodo*comprimentoComodo
    areaTotal += areaComodo
    print("A área do seu cômodo é:",areaComodo)
    continuar = input("Deseja continuar?")
    if continuar.casefold() in ["nao", "não", "n"]:
        queroContinuar = False

print("A área total dos cômodos calculados é de", areaTotal)