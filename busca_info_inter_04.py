import requests
from bs4 import BeautifulSoup

site_html = requests.get('https://www.climatempo.com.br/').content
soup = BeautifulSoup(site_html, 'html.parser')

print(soup.get_text())