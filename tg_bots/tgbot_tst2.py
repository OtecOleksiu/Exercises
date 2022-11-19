from bot1_token import token2
import requests
from bs4 import BeautifulSoup

import asyncio
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

bot = Bot(token=token2)

dp = Dispatcher(bot)

url1 = 'https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=qa&search_field=name&excluded_text' \
       '=&salary=&currency_code=RUR&experience=noExperience&schedule=remote&order_by=publication_time' \
       '&search_period=1&items_on_page=50 '

url2 = 'https://hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=NAME%3A%28Python+or+разработчик+or' \
       '+программист%29+AND+DESCRIPTION%3A%28Python%29&excluded_text=&salary=&currency_code=RUR&experience' \
       '=noExperience&schedule=remote&order_by=publication_time&search_period=3&items_on_page=100 '


headers1 = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0',
    'Accept': 'text/html'
}

url_weather = 'https://www.gismeteo.kz/weather-astana-5164/now/'
url_curs = 'https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut'


def get_weather():
    req = requests.get(url_weather, headers=headers1).text
    soup1 = BeautifulSoup(req, 'lxml')

    curr_weather = soup1.find(class_='unit unit_temperature_c').text.strip()
    return curr_weather


def get_currency():
    req1 = requests.get(url_curs, headers=headers1).text
    soup2 = BeautifulSoup(req1, 'lxml')

    currency = soup2.find(class_='table-responsive mb-4').find_all('tr')
    for i in currency:
        if i.find('td', text='USD / KZT') != None:
            return i.text.strip().replace('1 ДОЛЛАР США', '')


def hh_qa(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9 '
    }

    req = requests.get(url=url, headers=headers).text

    soup = BeautifulSoup(req, 'lxml')

    card_url = soup.find_all('a', class_='serp-item__title')

    urlz = []
    for url in card_url:
        urlz.append(url.get('href').split('?')[0])

    result_lst = []
    for i in urlz:
        req2 = requests.get(url=i, headers=headers).text

        soup2 = BeautifulSoup(req2, 'lxml')

        try:
            title = soup2.find('h1', class_='bloko-header-section-1').text
        except:
            title = 'the job has no name'
        try:
            salary = soup2.find(class_='bloko-header-section-2 bloko-header-section-2_lite').text
        except:
            salary = 'ypu will work for free'
        try:
            exp = soup2.find('p', class_='vacancy-description-list-item').text.split(': ')[1]
        except:
            exp = '200+ years in all possible languages'
        try:
            emp_mode = soup2.find(
                attrs={'class': 'vacancy-description-list-item', 'data-qa': 'vacancy-view-employment-mode'}).text
        except:
            emp_mode = 'idk how we gonna employ you'
        try:
            company = soup2.find('div', class_='vacancy-company-redesigned').find(
                class_='bloko-header-section-2 bloko-header-section-2_lite').text
        except:
            company = 'Apple, I swear'

        # ffs will finish job description later

        # requirements = soup2.find('div', class_='vacancy-description').find('div', class_='vacancy-section').find('div', class_='g-user-content')
        # requirements = soup2.find('div', class_='g-user-content').find(
        #     attrs={'strong', {'title': 'We offer:'}}).text
        # req = requirements.find_all('strong')
        # requirements = soup2.find_all('span')
        # print(requirements)
        # except:
        # raise Exception('...')
        # ...
        try:
            key2 = []
            key_val = soup2.find_all('div', class_='bloko-tag bloko-tag_inline')
            for key1 in key_val:
                key2.append(key1.text)
            key2 = ', '.join(key2)
        except:
            key2 = 'you have no talents'

        try:
            date_src = soup2.find('div', class_='bloko-gap bloko-gap_bottom').text.split(' ')[2]
            date_day = date_src.split('\xa0')[0]
            date_month = date_src.split('\xa0')[1]
            date_year = date_src.split('\xa0')[2]
            date = f'{date_day} {date_month} {date_year}'
        except:
            date = 'time is subjective'

        result_dict = {
            'date': date,
            'title': title.replace('\xa0', ' '),
            'salary': salary.replace('\xa0', ' '),
            'exp': exp.replace('\xa0', ''),
            'emp_mode': emp_mode.replace('\xa0', ' '),
            'company': company.replace('\xa0', ' '),
            'key_values': key2.replace('\xa0', ' ')

        }

        result_lst.append(result_dict)
        # result_lst.append('|'*10)

    return result_lst


@dp.message_handler(commands=['start'])
async def start_command(message):
    kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('hh_QA')
    btn2 = types.KeyboardButton('hh_Py')
    btn3 = types.KeyboardButton('weather in Astana now')
    btn4 = types.KeyboardButton('USD / KZT')
    kb1.add(btn1, btn2, btn3, btn4)
    await bot.send_message(message.from_user.id, f'Welcome, {message.from_user.first_name}. Push them buttons', reply_markup=kb1)


# @dp.message_handler(commands=['hh_QA'])
# async def hh_qa(message):
#     await bot.send_message(message.from_user.id, f'{hh_qa(url1)}')
#
#
# @dp.message_handler(commands=['hh_Py'])
# async def hh_py(message):
#     for i in range(len(hh_qa(url2))):
#         await bot.send_message(message.from_user.id, f'sending {i+1}/{len(hh_qa(url2))}')
#         await bot.send_message(message.from_user.id, f'{hh_qa(url2)[i]}')

@dp.message_handler(content_types=['text'])
async def tst3(message):
    if message.chat.type == 'private':
        if message.text == 'weather in Astana now':
            await bot.send_message(message.from_user.id, f'{get_weather()}')
        elif message.text == 'USD / KZT':
            await bot.send_message(message.from_user.id, f'{get_currency()}')
        elif message.text == 'hh_QA':
            for j in range(len(hh_qa(url1))):
                await bot.send_message(message.from_user.id, f'sending {j + 1}/{len(hh_qa(url1))}')
                await bot.send_message(message.from_user.id, f'{hh_qa(url1)[j]}')
        elif message.text == 'hh_Py':
            for i in range(len(hh_qa(url2))):
                await bot.send_message(message.from_user.id, f'sending {i + 1}/{len(hh_qa(url2))}')
                await bot.send_message(message.from_user.id, f'{hh_qa(url2)[i]}')
        else:
            await message.reply(message.text)
        #     await bot.send_message(message.chat.id, f'press a button')
    # await bot.send_message(message.from_user.id, f'{hh_qa(url2)}')


# @dp.message_handler()
# async def echo(message):
#     await message.reply(message.text)


# def main():
#     hh_qa()

# main()
# #

if __name__ == '__main__':
    executor.start_polling(dp)
