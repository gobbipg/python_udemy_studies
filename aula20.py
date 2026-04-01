# exercicio

primeiro_valor = int(input('digite um valor: '))
segundo_valor = int(input('digite outro valor: '))

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que o {segundo_valor=}')

elif primeiro_valor < segundo_valor:
    print(f'{segundo_valor=} é maior que o {primeiro_valor=}')

else:
    print('os valores são iguais')