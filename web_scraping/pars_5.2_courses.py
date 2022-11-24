import os
from random import randint
from time import sleep
from googletrans import Translator

import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.specialist.ru/profile/learning'
headers = {
    'Cookie': "SessionID=27daa6fd-0efb-41b6-b315-eb65452fb0a2; ASP.NET_SessionId=uh5w0fy3kxixir22dbvir4vi; userPollResWasShow=PollWasShow=1; CommonSite=1; .ASPXAUTH=C3A11ADEE233E6AF21938EF81451E66D4CDA2DADD7E79C1C9201BF902765513A6F360D7471D14F748CEC817ED4CA3A102F8832E12C7CBE9CA0BB9C1B2095F8F3D05B175C78DCA7EFB99A87ECC9A0FDD3C412DDF92F9B4E30782E8AC9DDE750FFD3B177752C9981D2ED8255359228C9F64276F2F1350D0C5F61741962656EFA397B77FAB439E96E88B70519C86DD7A053BF8943B61DF05A195E45F0448D9B3523; CookiePolice=1; VisitedCourses=0J7Qn9Cg0JLQldCRLdCQ'",
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

# req = requests.get(url, headers=headers).text

# with open('index_course.html', 'w') as file:
#     file.write(req)

translator = Translator()
with open('index_course.html') as file:
    src = file.read()

# print(req)

soup = BeautifulSoup(src, 'lxml')

urls = soup.find('div', class_='tab-zakonchennie tab_content2').find_all('a')

# print(urls)

urlz = []
for url in urls:

    if url.get('href').split('/')[1] == 'course':
        urlz.append(f"https://www.specialist.ru{url.get('href')}")
    else:
        continue

urlz.append('https://www.specialist.ru/course/python1-a')


result_lst = []
count = 0
for i in urlz:
    count += 1
    print(f'{count}/{len(urlz)}')
    url_print = f'{i[:33]}print/{i[33:]}'

    # this website either very protected from scraping or just works as shit, for only 1 out of 5-7 requests
    # were successfully and never all 10 in a row, so I had to first download necessary pages

    # if os.path.exists(f'C:/Users/m-gre/Desktop/IT/Python/1/web_scraping/course_tmp/index_page_{count}.html') == True:
    #     # print(f'skipping count {count}')
    #     # continue
    # else:
    #     req2 = requests.get(url_print, headers=headers).text
    #
    #     with open(f'course_tmp/index_page_{count}.html', 'w') as file:
    #         file.write(req2)

    with open(f'course_tmp/index_page_{count}.html') as file:
        src2 = file.read()

    soup2 = BeautifulSoup(src2, 'lxml')

    title = soup2.find('strong').text.strip()
    title = translator.translate(title, dest='en').text
    # print(title)
    subj = soup2.find_all(class_='td_subject')

    desc_list = []
    for j in subj:

        try:
            description = j.get_text().split('Примечание')[0].strip().replace('\n', ' ').replace('\t', '')  # HOW THE HELL IS THIS WORKING???????
            description = translator.translate(description, dest='en').text
        except:
            description = j.get_text().strip().replace('\n', ' ').replace('\t', '')
            description = translator.translate(description, dest='en').text
        # description = j.get_text().split('Примечание')[0].strip()
        desc_list.append(description)
    desc_list = desc_list[:-2]
    result_dict = {
        'title': title,
        'description': desc_list
    }

    result_lst.append(result_dict)
    print(f'done {count}')
    # maybe adding delay between requests would work, I thought. how naive.
    # zzz = randint(3,7)
    # print(f'sleeping {zzz} sec')
    # sleep(zzz)

with open('courses2_translated_to_eng.json', 'w', encoding='utf-8') as file:
    json.dump(result_lst, file, indent=4, ensure_ascii=False)

# with open('courses1.json', 'w', encoding='utf-8') as file:
#     json.dump(result_lst, file, indent=4, ensure_ascii=False)
