nome = 'Paulo'
sobrenome = 'Gobbi'
idade = 23
ano_nascimento = 2002
maior_de_idade = idade >= 18
altura_metros = 1.70

print('nome:', nome)
print('sobrenome:', sobrenome)
print('idade:', idade)
print('ano de nascimento:', ano_nascimento)
print('é maior de idade?:', maior_de_idade)
print('altura em metros:', altura_metros)

print('O', nome, sobrenome, 'tem', idade, 'anos de idade e nasceu em', str(ano_nascimento) + '. Sua altura é de', altura_metros, 'metros. Ele já é maior de idade?', maior_de_idade)
print(f'O {nome} {sobrenome} tem {idade} anos de idade e nasceu em {ano_nascimento}. Sua altura é de {altura_metros} metros. Ele já é maior de idade? {maior_de_idade}.') 

# o "f" antes de iniciar a string é utilizado para facilitar na hora de escrever no print e chamar as variáveis, colocando elas entre chaves...