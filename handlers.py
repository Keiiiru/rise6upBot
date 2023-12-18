from aiogram import types, Router
from aiogram.types import WebAppInfo
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart)
async def Start(m: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.KeyboardButton('Играть', web_app=WebAppInfo(url="https://rise6up.com/"))
    )
    await m.answer('Привет! Сыграть ты можешь нажав на кнопку', reply_markup=markup)
