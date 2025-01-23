from datetime import datetime

def get_current_date():
    """
    Retorna a data atual no formato YYYY-MM-DD.

    Returns:
        str: Data atual no formato YYYY-MM-DD.
    """
    return datetime.now().strftime('%Y-%m-%d')

def get_current_time():
    """
    Retorna a hora atual no formato HH:MM:SS.

    Returns:
        str: Hora atual no formato HH:MM:SS. 
    """
    return datetime.now().strftime('%H:%M:%S')

def format_date(date, format='%Y-%m-%d'):
    """
    Formata uma data para o formato especificado e retorna como string.

    Args:
        date (datetime): Data a ser formatada.
        format (str): Formato da data. Padrão é '%Y-%m-%d
    
    Returns:
        str: Data formatada.
    """
    return date.strftime(format)


def get_timesamp():
    """
    Retorna o timestamp atual.

    Returns:
        str: Timestamp atual.
    """
    return datetime.now().timestamp()

def get_timesamp_formated():
    """
    Retorna o timestamp atual no formato %H:%M:%S %Y-%m-%d.

    Returns:
        str: Timestamp atual no formato %H:%M:%S %Y-%m-%d.
    """
    return datetime.now().strftime('%H:%M:%S-%Y-%m-%d')

# Exemplo de uso
if __name__ == "__main__":
    print(get_current_date())
    print(get_current_time())
    print(format_date(datetime.now()))
    print(get_timesamp())
    print(get_timesamp_formated())