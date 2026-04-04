"""
formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou x - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'abc'

print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel:0<10}.')
print(f'{variavel:-^10}.')

print(f'{1000.87642387564:0=+10,.1f}')

print(f'o hexadecimal de 1500 é {1500:08x}')