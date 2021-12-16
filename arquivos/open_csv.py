import csv

file = open('./arquivos/CSV.CSV', 'r')

reader = csv.reader(file, delimiter = ';')

for row in reader:
    print(row)

file.close()