# operadores lógicos 
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# se qualquer valor for considerado false, a expressão inteira será avaliada naquele valor.
# são consideradas falsy (que vc já viu)
# 0, 0.0, '', False
# também existe o tipo None que é 
# usado para representar um não valor.

entrada = input('[E]ntrar ou [S]air: ')
senha = input('Digite a senha: ')
senha_permitida = '12345'

if entrada == 'E' and senha == senha_permitida:
    print('Você está logado!')

else:
    print('Você saiu!')

# avaliação de curto circuito
print(True and True and True) # True
print(True and False and True) # False
print(True and 0 and True) # 0 False
print(bool('')) # False