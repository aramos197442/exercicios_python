#####################################################################################################
# Este pequeno programa cria uma arquivo de configurações chamado configurations.ini
#no diretório config_files_example e o usa para guardar e apresentar em tela itens de configuração
#####################################################################################################


import configparser

# Criar o objeto
config_file = configparser.ConfigParser()

# Adicionar sessão
config_file.add_section("FTPSettings")
# Adicionar configurações
config_file.set("FTPSettings", "ftpUrl", "demoftp.codeteddy.com")
config_file.set("FTPSettings", "userName", "codeteddy")
config_file.set("FTPSettings", "password", "minha#senha")

# SEGUNDO PASSO
# Adicionar uma sessão LOGGER com configurações
config_file["Logger"]={
    "LogFilePath":"<Caminho para o arquivo de log",
    "LogFileName":"<Nome do arquivo de log",
    "LogLevel":"Info"
}
# FIM DO SEGUNDO PASSO

# Salvar arquivo
with open("./config_files_example/configurations.ini", "w") as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Arquivo de configuração 'configurations.ini' criado!")

# Imprimir conteúdo do arquivo
read_file = open("./config_files_example/configurations.ini", "r")
content = read_file.read()
print("O conteúdo do arquivo de configuração é: \n")
print(content)
read_file.flush()
read_file.close()