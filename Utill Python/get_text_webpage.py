import requests
from bs4 import BeautifulSoup

def extract_text(url):
    """
    Função para extrair texto de uma página da web. 

    Args:
        url (str): URL da página da web.

    Returns:
        str: Texto extraído da página da web.
    """
    # Faz uma requisição GET para a URL
    response = requests.get(url)
    
    # Parseia o conteúdo da página com BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extrai o texto de todos os parágrafos da página
    paragraphs = soup.find_all('p')
    text = ' '.join([p.get_text() for p in paragraphs])
    
    return text

# Exemplo de uso
url = 'https://stackoverflow.com/questions/18831380/how-can-i-from-bs4-import-beautifulsoup'
extracted_text = extract_text(url)
print(extracted_text)
