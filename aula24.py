# operadores in e not in
# strings são iteráveis
# 0 1 2 3 4 5
# o t á v i o
#-6-5-4-3-2-1

nome = 'otávio'

print(nome[2])
print(nome[-4])
print('a' in nome)
print('á' in nome)
print('-' * 10)
print('vio' not in nome)
print('oba' not in nome)

nome1 = input('digite seu nome: ')
encontrar = input('digite o que deseja encontrar: ')

if encontrar in nome1:
    print(f'{encontrar} está entre {nome1}')

else:
    print(f'{encontrar} não está entre {nome1}')