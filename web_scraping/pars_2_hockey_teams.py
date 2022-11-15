import requests
from bs4 import BeautifulSoup
import json

# url = 'https://www.scrapethissite.com/pages/forms/'
#
# req = requests.get(url).text
# with open('index_hockey.html') as file:
#     file.write(req)

with open('index_hockey.html') as file:
    src = file.read()
all = []
headers = []
soup = BeautifulSoup(src, 'lxml')
header = soup.find(class_='table').find_all('th')

for j in header[:4]:
    x = j.text.strip()
    headers.append(x)

for i in range(1, 25):
    url = f'https://www.scrapethissite.com/pages/forms/?page_num={i}'
    print(i)
    req = requests.get(url).text

    soup1 = BeautifulSoup(req, 'lxml')

    teams = soup1.find_all(class_='team')

    for team in teams:
        team_name = team.find(class_='name').text.strip()
        year = team.find(class_='year').text.strip()
        wins = team.find(class_='wins').text.strip()
        losses = team.find(class_='losses').text.strip()
        all1 = {headers[0]: team_name,
                headers[1]: year,
                headers[2]: wins,
                headers[3]: losses}

        all.append(all1)

with open('hockey_teams.json', 'w', encoding='utf-8') as file:
    json.dump(all, file, indent=4, ensure_ascii=False)
# print(all)
