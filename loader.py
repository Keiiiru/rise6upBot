from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

bot = Bot(config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
