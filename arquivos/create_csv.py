import csv

file = open('./arquivos/CSV.CSV', 'w')

# O método writer em csv.writer sem o parâmetro "delimiter = ';'" faria com que o arquivo usasse a , (vírgula) como é tradicional nos arquivos CSV
writer = csv.writer(file, delimiter = ';')

keys = ['nome', 'peso', 'sexo', 'idade']
writer.writerow(keys)

rows = [
    ['leo', 82, 'M', 26],
    ['berenice', 89, 'F', 65],
    ['ilda', 61, 'F', 77],
    ['henrique', 25, 'M', 11],
    ['barbara', 57, 'F', 18]
]

writer.writerows(rows)

file.close()