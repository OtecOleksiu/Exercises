import requests
import json

megalist =[]
megalist2 =[]
for i in range(5, -1, -1):
    print(i)
    url = f'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=201{i}'
    req = requests.get(url).text.strip()
    req = json.loads(req)
    megalist.append(req)

for j in megalist:
    for k in j:
        megalist2.append(k)

with open('oscar_films.json', 'w', encoding='utf-8') as file:
    json.dump(megalist2, file, indent=4, ensure_ascii=False)
