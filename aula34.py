"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira (True)
loop infinito -> quando o código não tem fim
"""

# condicao = True

# while condicao:
#     print('loop')

while True:
    nome = input('digite seu nome: ')
    print(f'seu nome é {nome}')
    if nome == 'sair':
        break 

print('fim do loop')