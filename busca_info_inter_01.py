import requests
from bs4 import BeautifulSoup

site_html = requests.get('https://www.climatempo.com.br/').content
soup = BeautifulSoup(site_html, 'html.parser')
# print(soup.find_all('li')) # Realiza busca de todas as tags

varialvel = soup.find_all('a')
for links in varialvel:
    strings_1 = links.string
    strings_2 = links.get('href')
    print('-' * 30)
    print(strings_1)    
    print(strings_2)
