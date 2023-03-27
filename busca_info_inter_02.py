import requests
from bs4 import BeautifulSoup

site_html = requests.get('https://www.climatempo.com.br/').content
soup = BeautifulSoup(site_html, 'html.parser')

busca_1 = soup.find_all('a')
for links in busca_1:
    print(links.get('href'))
