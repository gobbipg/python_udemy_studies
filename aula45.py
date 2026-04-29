"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Luiz') # __iter__()
# print(next(texto)) # __next__()
# print(next(texto)) # __next__()
# print(next(texto)) # __next__()
# print(next(texto)) # __next__()

# for letra in texto
texto = 'Luiz' # iterável
iterador = iter(texto) # iterator

# como é o for por debaixo dos panos:

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)