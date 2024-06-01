# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python e laço de repetição While

# Apresentar todos os valores numéricos inteiros ímpares situados na faixa de 0 a 20.
# Para verificar se o número é ímpar, efetuar dentro da malha a verificação lógica
# desta condição com a instrução se, perguntando se o número é ímpar; sendo, mostre-o;
# não sendo, passe para o próximo passo.

numeros = 0

while numeros < 21:
    if numeros % 2 == 1:
        print(numeros)
    numeros += 1