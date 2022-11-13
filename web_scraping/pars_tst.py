import requests
from bs4 import BeautifulSoup
import json

# url = 'https://www.scrapethissite.com/pages/simple/'
#
# req = requests.get(url).text
#
# with open('scrap1_countries.html', 'w', encoding='utf-8') as file:
#     file.write(req)

with open('scrap1_countries.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

country_name_all = soup.find_all(class_='col-md-4 country')

all2 = []
for i in country_name_all:
    country_name = i.find(class_='country-name').text.strip()
    capital = i.find(class_='country-capital').text.strip()
    population = i.find(class_='country-population').text.strip()
    area = i.find(class_='country-area').text.strip()
    all1 = {'country_name': country_name,
            'capital': capital,
            'population': population,
            'area': area}
    all2.append(all1)

with open('1.json', 'w', encoding='utf-8') as file:
    json.dump(all2, file, indent=4, ensure_ascii=False)
