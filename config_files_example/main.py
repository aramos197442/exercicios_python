# Importar o novo método read_config do arquivo helper.py
import helper

config = helper.read_config()

#### O que era antes um simples conjunto de variáveis de texto...
# ftpUrl = "demoftp.codeteddy.com"
# userName = "codeteddy"
# password = "meu#segredo"
#### ... passa a ser um conjunto de variáveis que recebem informações do arquivo de configurações 'coonfigurations.ini'
ftpUrl = config['FTPSettings']['ftpUrl']
userName = config['FTPSettings']['userName']
password = config['FTPSettings']['password']


print("\nDetalhes de FTP")

print("FTP URL: "+ftpUrl)
print("FTP User Name: "+userName)
print("Password: "+password)