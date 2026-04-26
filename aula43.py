# Se tem lista ou uma sequência, o melhor é o for
# Se tem condição aberta em que você não sabe quando vai acabar, o melhor é o while

# texto = 'Python'
# i = 0

# while i < len(texto):
#     print(texto[i], i)

#     i += 1

texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)