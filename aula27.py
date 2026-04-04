"""
fatiamento de strings
 012345678
 Olá mundo
-987654321
fatiamento [i:f:p] [::] - i= inicio - f= final - p= passos
obs.: a função len retorna a qtd de caracteres da str
"""

variavel = 'olá mundo'

# nesse print, eu quero que comece do "m" e pare la no "d".
print(variavel[4:8]) # em python, normalmente o índice final não aparece. Nesse caso, precisa colocar um índice a+ para pegar o índice desejado...

print(len(variavel[3])) # estou contando somente a qtd de índice que solicitei, no caso o índice "3" (que seria o espaço do "olá mundo").
print(len(variavel)) # estou contando a qtd de caracteres dessa string (variavel).

# pode só colocar a qtd da string em vez de usar ":len(variavel):". Como está no segundo print.
print(variavel[0:len(variavel):2]) # aqui estou pulando as "casas" nos índices. Pulando de dois em dois...
print(variavel[-1:-10:-2]) # aqui estou pulando as "casas" nos índices. Pulando de dois em dois mas utilizando os índices negativos...