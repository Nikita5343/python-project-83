from bs4 import BeautifulSoup
import requests

def get_data(url):
    try:
        response = requests.get(url.name, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        h1 = soup.h1.get_text().strip() if soup.h1 else None
        title = soup.title.string.strip() if soup.title else None
        description = soup.find(
            'meta', 
            attrs={'name': 'description'}
        )
        description = (description['content'].strip() 
                    if description else None)
        return h1, title, description
    except Exception as e:
        print(e)