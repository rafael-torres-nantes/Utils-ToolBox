import subprocess

def run_subprocess(command):
    """
    Executa um comando no terminal e retorna o resultado.
    
    Args:
        command (list): Lista com os argumentos do comando.
    """
    result = subprocess.run(command, capture_output=True, text=True)
    return result

# Exemplo de uso
if __name__ == '__main__':
    command = ['mkdir', 'teste']
    result = run_subprocess(command)
    print(result.stdout)
