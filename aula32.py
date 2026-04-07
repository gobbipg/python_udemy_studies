"""
1- Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# Jeito que eu tentei:
numero = int(input('Digite um número inteiro: '))

if (numero % 2) == 0:
    print('O número é par.')
elif (numero % 2) == 1:
    print('O número é ímpar.')
else:
    print('Você não digitou um número inteiro.')

# Jeito que o professor fez:
entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro.')

"""
2- Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# Jeito que eu tentei:
hora = float(input('Digite um horário: '))

if hora >= 0 and hora <= 11:
    print('Bom dia!')
elif hora >= 12 and hora <= 17:
    print('Boa tarde!')
else:
    print('Boa noite!')

# Jeito que o professor fez:
entrada_1 = input('Digite a hora em números inteiros: ')

try:
    hora_1 = int(entrada_1)

    if hora_1 >= 0 and hora_1 <= 11:
        print('Bom dia!')
    elif hora_1 >= 12 and hora_1 <= 17:
        print('Boa tarde!')
    elif hora_1 >= 18 and hora_1 <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora.')

except:
    print('Por favor, digite apenas números inteiros.')

"""
3- Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Jeito que eu tentei:
nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto!')
elif len(nome) == 5 or len(nome) == 6:
    print('Seu nome é padrão!')
elif len(nome) > 6:
    print('Seu nome é grande.')

# Jeito que o professor fez:
nome_1 = input('Digite seu nome: ')
tamanho_nome = len(nome_1)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')

else:
    print('Digite mais de uma letra.')