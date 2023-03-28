import requests
import lxml
from bs4 import BeautifulSoup

busca_2 = []

site_html = requests.get('https://www.climatempo.com.br/').content
soup = BeautifulSoup(site_html, 'lxml')

busca_1 = soup.find_all('a')
for valor in busca_1:
    busca_2.append(valor)

for links in enumerate(busca_2):
    if links == soup.get('href'):
        print(links)

print('ERRO')
