# Curso Básico de Python
# Nome do Desenvolvedor: Victor Fregni Gogorza
# Versão1.0
# Exercício de lógica de programação utilizando a linguagem de programação Python e laço de repetição While

# Apresentar o total da soma obtida dos cem primeiros números inteiros (1+2+3+4+...+98+99+100).


contadora = 1
soma = 0
while contadora <101:
    soma += contadora
    contadora += 1
print(soma)