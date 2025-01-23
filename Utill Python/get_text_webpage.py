import requests
from bs4 import BeautifulSoup # beautifulsoup4

# pip install beautifulsoup4

def extract_text(url):
    # Fetch the webpage content
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract text from all paragraph tags
    paragraphs = soup.find_all('p')
    text = ' '.join([p.get_text() for p in paragraphs])
    
    return text

# Example usage
url = 'https://stackoverflow.com/questions/18831380/how-can-i-from-bs4-import-beautifulsoup'
extracted_text = extract_text(url)
print(extracted_text)
