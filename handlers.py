from datetime import datetime, timedelta

from aiogram import Bot, Router
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import (
    Message,
    MenuButtonWebApp,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from utils import generate_token

my_router = Router()


@my_router.message(CommandStart())
async def command_start_no_deep_link(
    message: Message, command: CommandObject, bot: Bot, base_url: str
):
    if command.args and len(command.args.split("_")) == 3:
        token = generate_token(
            {
                "uid": message.from_user.id,
                "exp": (datetime.now() + timedelta(minutes=30)).timestamp(),
                "act": command.args.split("_")[1],
            }
        )
        auth_link = "https://rise6up.com/login/telegram?token=" + token
        await message.answer(f"Ваша ссылка для авторизации: {auth_link}")
    else:
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
                        InlineKeyboardButton(
                            text="Открыть", web_app=WebAppInfo(url=f"{base_url}demo")
                        )
                    ]
                ]
            ),
        )
