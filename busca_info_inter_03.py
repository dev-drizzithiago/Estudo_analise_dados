import requests
from bs4 import BeautifulSoup

site_html = requests.get('https://www.climatempo.com.br/').content
soup = BeautifulSoup(site_html, 'html.parser')

dados = soup.find("span", class_="_block _margin-b-5 -gray")
temperatura = dados.string
for temp in temperatura:
    print(temperatura)
