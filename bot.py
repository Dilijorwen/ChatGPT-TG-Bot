# Это нужные нам библиотеки
import asyncio
import logging
import sys
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers import start_handler
from handlers import help_handler
from handlers import dice_handler

async def main() -> None:
    # Функция, которая подгружает ключ – значения из “.env
    load_dotenv()

    # Здесь мы присеваем переменной TOKEN значение, котрое он вытащил по ключу из “.env”.
    TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

    # Объявляем диспечер
    dp = Dispatcher()

    # Добовляем в наш диспечер роутеры
    dp.include_routers(start_handler.router, help_handler.router, dice_handler.router)


    #Объявили бота с токеном c парс модом, который будет форматировать сообщения
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    #Начинаем полинг
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Логирование, оно нужно, чтобы мне не пропустили важные сообщения в консоли
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())