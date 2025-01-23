# filepath: /path/to/file_utils.py
import os

def read_file(file_path):
    """
    Lê o conteúdo de um arquivo e retorna como string.
    
    Args:
        file_path (str): Caminho do arquivo.
    """
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    """
    Escreve uma string em um arquivo no caminho especificado.
    
    Args:
        file_path (str): Caminho do arquivo.
        content (str): Conteúdo a ser escrito no arquivo.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def list_files(directory):
    """
    Lista todos os arquivos em um diretório.
    
    Args:
        directory (str): Caminho do diretório.
    """
    return os.listdir(directory)

def search_extension_in_directory(directory, extension='.md'):
    """
    Procura por arquivos com uma extensão específica em um diretório.

    Args:
        directory (str): Caminho do diretório.
    """

    # Lista de arquivos com a extensão especificada
    extension_files = []

    # Percorre o diretório e seus subdiretórios
    for root, dirs, files in os.walk(directory):

        # Crie um filtro para selecionar apenas arquivos com a extensão especificada
        extension_files = [os.path.join(root, file) for file in files if file.endswith(extension)]

    return extension_files


# Exemplo de uso
if __name__ == "__main__":
    print(search_extension_in_directory('.'))