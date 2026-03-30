# \r\n quebra de linha padrão do windows
print(12, 34, 1234, sep="-") # ctrl + c e depois ctrl + v na linha selecionada, você duplica a linha selecionada para baixo dela.
print(25, 67, sep='-') # sep= é utilizado para alterar a forma que os parâmetros estão sendo separados...
print(25, 67, sep='-', end='\r\n')
print(25, 67, sep='-', end='\n##')