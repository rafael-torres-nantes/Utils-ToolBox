import uuid
import hashlib

def generate_unique_id():
    """
    Gera um ID único usando a biblioteca uuid.
    """
    return str(uuid.uuid4())

def generate_hashed_id(input_string):
    """
    Gera um ID único a partir de uma string de entrada.

    Args:
        input_string (str): String de entrada.
    """
    return hashlib.sha256(input_string.encode()).hexdigest()

# Exemplo de uso
if __name__ == "__main__":
    print(generate_unique_id())
    print(generate_hashed_id('example_string'))