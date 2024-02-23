from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import (
    Message,
    MenuButtonWebApp,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

my_router = Router()


@my_router.message(Command("start"))
async def command_start(message: Message, bot: Bot, base_url: str):
    await bot.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=MenuButtonWebApp(
            text="Открыть", web_app=WebAppInfo(url=f"{base_url}demo")
        ),
    )
    await message.answer(
        "Привет! Сыграть ты можешь нажав на кнопку!",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Открыть", web_app=WebAppInfo(url=f"{base_url}demo"))
                ]
            ]
        )
    )

