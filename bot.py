# Это нужные нам библиотеки
import asyncio
import logging
import sys
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.filters.command import CommandStart, Command
from aiogram.types import Message

# Функция, которая подгружает ключ – значения из “.env
load_dotenv()
# Здесь мы присеваем переменной TOKEN значение, котрое он вытащил по ключу из “.env”.
TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
# Объявляем диспечер
dp = Dispatcher()

@dp.message(CommandStart()) #Вот так выглядит декоратор
# Мы можем записать его так:@dp.message(Command("start"))
# Хэндлер для команды /start
async def command_start_handler(message: Message) -> None:
    # await - требование к вызову функции для асинхронки
    # После messeage стоит дополнение к функции, которое говорит, что бот сделает
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}! \nНапиши /help")

@dp.message(Command("help"))
async def command_start_handler(message: Message) -> None:
    await message.reply("Привет! Я тестовый бот для методички.\n"
                         "Я умею повторять за тобой сообщения и пока все)))")

@dp.message()
async def echo_handler(message: Message) -> None:
    # Использум блок try-cacth
    try:
        await message.send_copy(chat_id=message.chat.id)
    except ValueError:
        await message.answer("Я не поддерживаю данный тип сообщений")


async def main() -> None:
    #Объявили бота с токеном
    bot = Bot(token=TOKEN)
    #Начинаем полинг
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())