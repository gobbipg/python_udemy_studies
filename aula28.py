"""
exercício:
peça ao usuário para digitar seu nome
peça ao usuário para digitar sua idade
se nome e idade forem digitados:
    exiba:
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        seu nome contém {ou não} espaços
        seu nome tem {n} letras
        a primeira letra do seu nome é {letra}
        a úutima letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba "desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}') # jeito simples de inverter um texto
    
    if ' ' in nome:
        print('seu nome contém espaços.')
    else:
        print('seu nome não contém espaços.')

    print(f'Seu nome tem: {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')

else:
    print('Desculpe, você deixou campos vazios.')