file = open('./arquivos/nomes.txt', 'r')

for i in range(4):
    print(file.readline())

file.close()