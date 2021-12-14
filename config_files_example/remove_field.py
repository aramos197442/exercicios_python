import configparser

# Criar objeto
config_file = configparser.ConfigParser()

# Ler o arquivo de configuração
config_file.read("./config_files_example/configurations.ini")

# Apagar o campo Format da sessão Logger
config_file.remove_option("Logger","Format")

# Salvar as configurações no arquivo
with open("./config_files_example/configurations.ini", "w") as file_object:
    config_file.write(file_object)

# Mostrar configurações atualizadas
print("Arquivo de configurações 'configurations.ini' foi atualizado!")
print("São as configurações atualizadas:\n")
file=open("./config_files_example/configurations.ini", "r")
settings=file.read()
print(settings)