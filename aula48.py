"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Méetodos úteis: append, insert, pop, del, clear, extend, +
"""
#         01234
#        -54321
string = 'ABCDE' # 5 caracteres (len = quantidade)
# print(bool([])) # falsy
# print(lista, type(lista))

#        0      1      2      3    4
#       -5     -4     -3     -2   -1
lista = [123, True, 'gobbi', 1.1, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2].upper(), type(lista[2]))
