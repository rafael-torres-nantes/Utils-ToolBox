# filepath: /path/to/list_utils.py
def flatten_list(nested_list):
    """
    Achata uma lista aninhada em uma lista simples.

    Args:
        nested_list (list): Lista aninhada.
    """
    return [item for sublist in nested_list for item in sublist]

def unique_elements(input_list):
    """
    Retorna uma lista com elementos únicos de uma lista de entrada.

    Args:
        input_list (list): Lista de entrada.
    """
    return list(set(input_list))

def sort_list(input_list):
    """
    Ordena uma lista de entrada.
    
    Args:
        input_list (list): Lista de entrada.
    """
    return sorted(input_list)

# Exemplo de uso
if __name__ == "__main__":
    print(flatten_list([[1, 2], [3, 4]]))
    print(unique_elements([1, 2, 2, 3, 4, 4]))
    print(sort_list([4, 2, 3, 1]))