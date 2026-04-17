""" Calculadora com while """
while True:

    ...

    sair = input('Deseja sair? Digite [s]: ').lower().startswith('s')
    # lower: deixa toda a string com letras minusculas (mesmo se o usuario digitar com maiusculas).
    # startswith: retorna um bool caso o usuario digite algo que comece com alguma letra especifica (nesse caso se ele digitar "s" vai fechar o while...)
    if sair is True:
        break
