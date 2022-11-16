import requests
from bs4 import BeautifulSoup
import json

# url = 'https://www.scrapethissite.com/pages/frames/?frame=i'
#
# req = requests.get(url).text
#
# with open('index_turtles.html', 'w') as file:
#     file.write(req)

with open('index_turtles.html') as file:
    src = file.read()


soup = BeautifulSoup(src, 'lxml')

href_classes = soup.find_all(class_='col-md-4 turtle-family-card')
src_url = []
for i in href_classes:
    urls = 'https://www.scrapethissite.com' + f"{i.find('a').get('href')}"
    src_url.append(urls)

result = []
count = 0
for j in src_url:
    count += 1
    print(count)
    req = requests.get(j).text
    soup1 = BeautifulSoup(req, 'lxml')
    img_url = soup1.find(class_='col-md-6 col-md-offset-3 turtle-family-detail').find('img').get('src')
    family_name = soup1.find(class_='family-name').text
    description = soup1.find(class_='col-md-6 col-md-offset-3 turtle-family-detail').find('p').text.strip().replace('"', '\'')

    res_dict = {
        'img_url':img_url,
        'family_name':family_name,
        'description':description
    }
    result.append(res_dict)

with open('turtles.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
