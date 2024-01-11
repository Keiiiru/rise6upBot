import logging
import sys

from aiohttp.web import run_app
from aiohttp.web_app import Application
from aiogram import Bot, Dispatcher
from aiogram.types import MenuButtonWebApp, WebAppInfo
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

import config
from handlers import my_router
from routes import demo_handler


async def on_startup(bot: Bot, base_url: str):
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="Open Menu", web_app=WebAppInfo(url=f"{base_url}/demo")
        )
    )


def main():
    bot = Bot(token=config.TOKEN, parse_mode="HTML")
    dispatcher = Dispatcher()
    dispatcher["base_url"] = config.APP_BASE_URL
    dispatcher.startup.register(on_startup)

    dispatcher.include_router(my_router)

    app = Application()
    app["bot"] = bot

    app.router.add_get("/demo", demo_handler)
    setup_application(app, dispatcher, bot=bot)

    run_app(app, host="0.0.0.0", port=8081)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    main()
