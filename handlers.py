from aiogram import types
from aiogram.types import WebAppInfo
from aiogram.dispatcher.filters import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def start_handler(m: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.KeyboardButton('Играть', web_app=WebAppInfo(url="https://rise6up.com/"))
    )
    await m.answer('Привет! Сыграть ты можешь нажав на кнопку!', reply_markup=markup)
