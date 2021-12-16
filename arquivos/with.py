# Uso do bloco 'with'
with open("./arquivos/hello_world.txt") as file:
    print(file.read())
# ...percebe-se que com o bloco 'with' não há a necessidade de fechar o arquivo com 'file.close()'

# Um erro acontecerá na execução da linha abaixo pois o bloco 'with' já foi fechado
print(file.read())
