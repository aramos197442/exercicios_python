import configparser

# Criar método para ler o arquivo de configurações
def read_config():
    config = configparser.ConfigParser()
    config.read('./config_files_example/configurations.ini')
    return config