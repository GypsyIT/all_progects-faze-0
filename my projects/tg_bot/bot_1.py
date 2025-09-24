import logging
from string import punctuation
from dotenv import load_dotenv
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command


load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message(Command(commands=['start']))
async def start_bot(messenge: Message):
    user_id = messenge.from_user.id
    user_full_name = messenge.from_user.full_name
    text_for_user = f'Привет, {user_full_name}!'
    text_for_user_2 = f'Я бот, который переведет твое ФИО с кириллицы в латиницу в соответствии с Приказом МИД России от 12.02.2020 № 2113. Давай попробуем? :)'
    logging.info(f'ID: {user_id}, Name: {user_full_name} запустил бота')
    await bot.send_message(chat_id=user_id, text=text_for_user)
    await bot.send_message(chat_id=user_id, text=text_for_user_2)

@dp.message()
async def messege_in_bot(messenge: Message):
    letter = {
        'а': 'a',
        'А': 'A',
        'б': 'b',
        'Б': 'B',
        'в': 'v',
        'В': 'V',
        'г': 'g',
        'Г': 'G',
        'д': 'd',
        'Д': 'D',
        'е': 'e',
        'Е': 'E',
        'ё': 'e',
        'Ё': 'E',
        'ж': 'zh',
        'Ж': 'ZH',
        'з': 'z',
        'З': 'Z',
        'и': 'i',
        'И': 'I',
        'й': 'i',
        'Й': 'I',
        'к': 'k',
        'К': 'K',
        'л': 'l',
        'Л': 'L',
        'м': 'm',
        'М': 'M',
        'н': 'n',
        'Н': 'N',
        'о': 'o',
        'О': 'O',
        'п': 'p',
        'П': 'P',
        'р': 'r',
        'Р': 'R',
        'с': 's',
        'С': 'S',
        'т': 't',
        'Т': 'T',
        'у': 'u',
        'У': 'U',
        'ф': 'f',
        'Ф': 'F',
        'х': 'kh',
        'Х': 'KH',
        'ц': 'ts',
        'Ц': 'TS',
        'ч': 'ch',
        'Ч': 'CH',
        'ш': 'sh',
        'Ш': 'SH',
        'щ': 'shch',
        'Щ': 'SHCH',
        'ы': 'y',
        'Ы': 'Y',
        'ъ': 'ie',
        'Ъ': 'IE',
        'э': 'e',
        'Э': 'E',
        'ю': 'iu',
        'Ю': 'IU',
        'я': 'ia',
        'Я': 'IA',
        'ь': '',
        'Ь': '',
        ' ': ' '
    }
    user_id = messenge.from_user.id
    user_full_name = messenge.from_user.full_name
    text = messenge.text
    result = ''
    for l in text:
        if (letter.get(l, '-') == '-'):
            return messenge.answer(text='Ошибка! Введите текст только кирилицей!')
        elif l in punctuation:
            return messenge.answer(text='Ошибка! Сообщение содежит символы не соответвующие буквам!')
        else:
            result += l.replace(l, letter[l])
    logging.info(f'ID: {user_id}, Name: {user_full_name}, Messenge: {text}')
    await messenge.answer(text=result)

if __name__ == '__main__':
    dp.run_polling(bot)