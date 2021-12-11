lista_estudantes = ['Marcela','Lucas','Leonardo','Alexandre','Cristiane']

for i in range(len(lista_estudantes)):
    print(lista_estudantes[i])
    lista_estudantes[i] = 'Pedro'
print('Lista de estudantes ao sair do bloco for: ', lista_estudantes)