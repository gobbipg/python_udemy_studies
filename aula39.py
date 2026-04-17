"""
Iterando strings com while
"""
# meu jeito:

# nome = input('Digite seu primeiro nome: ')
# novo_nome = len(nome)

# while novo_nome <= 10:
#     print(nome)
#     novo_nome += 1

# print('Acabou')

# Jeito do professor:

nome = input('Digite seu nome: ')

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'{letra}*'
    indice += 1

print(novo_nome)