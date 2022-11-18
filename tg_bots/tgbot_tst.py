import requests
from bs4 import BeautifulSoup
from bot1_token import token
import telebot
from telebot import types

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0',
    'Accept': 'text/html'
}

url_weather = 'https://www.gismeteo.kz/weather-astana-5164/now/'
url_curs = 'https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut'


def get_weather():
    req = requests.get(url_weather, headers=headers).text
    soup1 = BeautifulSoup(req, 'lxml')

    curr_weather = soup1.find(class_='unit unit_temperature_c').text.strip()
    return curr_weather


def get_currency():
    req1 = requests.get(url_curs, headers=headers).text
    soup2 = BeautifulSoup(req1, 'lxml')

    currency = soup2.find(class_='table-responsive mb-4').find_all('tr')
    for i in currency:
        if i.find('td', text='USD / KZT') != None:
            return i.text.strip().replace('1 ДОЛЛАР США', '')


def tg_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, f'sup, {message.from_user.first_name}', reply_markup=kb1)

    kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('weather in Astana now')
    btn2 = types.KeyboardButton('USD / KZT')
    kb1.add(btn1, btn2)

    @bot.message_handler(content_types=['text'])
    def tst1(message):
        if message.chat.type == 'private':
            if message.text == 'weather in Astana now':
                bot.send_message(message.chat.id, f'{get_weather()}')
            elif message.text == 'USD / KZT':
                bot.send_message(message.chat.id, f'{get_currency()}')
            else:
                bot.send_message(message.chat.id, f'please press a button')

    bot.polling()


tg_bot(token)

