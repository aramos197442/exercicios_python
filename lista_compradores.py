compradores = ['Alexandre','Fernanda','Cristiane','Rodrigo','Barbara','Afonso','Paulo']

nome_digitado = input('Qual é seu nome: ')
for nome in compradores:
    print(nome)
    if(nome == nome_digitado):
        print('Ok, encontrado. Tome se ticket!!!')
        break