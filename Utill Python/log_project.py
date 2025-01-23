import logging

def setup_logger(name, log_file, level=logging.INFO):
    """
    Configura um logger para o projeto e salva os logs em um arquivo.

    Args:
        name (str): Nome do logger.
        log_file (str): Caminho do arquivo de log.
        level (int): Nível de log. Padrão é logging.INFO
    """
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Exemplo de uso
if __name__ == "__main__":
    logger = setup_logger('log_info', 'log_file.log')
    logger.info('Log de informação')