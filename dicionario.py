person_dict = {
    'nome':'Alexandre',
    'sexo':'Masculino',
    'idade':47,
    'peso':90
}

# O for abaixo traz o dicionario de chave:valor
for person in person_dict:
    print(F'{person}:{person_dict[person]}')

# Agora apenas o valor
for value in person_dict.values():
    print(value)

# e agora somente as chaves
for keys in person_dict.keys():
    print(keys)

if person_dict.get('nome'):
    print('Hey, {}! How you doing?'.format(person_dict.get('nome')))
else:
    print('Forget it!')
