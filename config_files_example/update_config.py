import configparser

# Criar objeto
config_file = configparser.ConfigParser()

# Ler o arquivo de configuração
config_file.read("./config_files_example/configurations.ini")

# Alterar o valor do campo LogLevel de 'Info' para 'Debug'
config_file["Logger"]["LogLevel"] = "Debug"

# Adicionar um novo campo sob a sessão Logger
config_file["Logger"].update({"Format":"(mensagem)"})

# Salvar as configurações no arquivo
with open("./config_files_example/configurations.ini", "w") as file_object:
    config_file.write(file_object)

# Mostrar configurações atualizadas
print("Arquivo de configurações 'configurations.ini' foi atualizado!")
print("São as configurações atualidas:\n")
file=open("./config_files_example/configurations.ini", "r")
settings=file.read()
print(settings)