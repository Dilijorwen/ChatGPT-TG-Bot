# Это нужные нам библиотеки
import asyncio
import logging
import sys
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html
from aiogram.filters.command import CommandStart, Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, KeyboardButton, KeyboardButtonRequestChat, KeyboardButtonPollType, KeyboardButtonRequestUser
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.utils.keyboard import ReplyKeyboardBuilder

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
    # massage.from_user.full_name - Определяет имя пользователья
    # html.bold - делает жирную разметку для имени пользователя в стиле html(для этого мы ниже делам parse_mode)
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}! \nНапиши /help")

@dp.message(Command("help"))
async def command_start_handler(message: Message) -> None:
    await message.reply("Привет! Я тестовый бот для методички\n"
                         "У менять есть селудующие команды:\n"
                        "/dice - мы с тобой кинем шестигранный кубик\n"
                        "/help - выведу тебе данное сообщение\n"
                        "А также могу повторять за тобой сообщения.")

@dp.message(Command("dice"))
async def dice_handler(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)

# Эта штука находиться внизу, потому что она принимает все сообщения, и если поставить ее наверх,
# то она примет даже “/help” и просто его повторит и не выведет нужную инфу
@dp.message()
async def echo_handler(message: Message) -> None:
    # Использум блок try...cacth
    try:
        await message.send_copy(chat_id=message.chat.id)
    except ValueError:
        await message.answer("Я не поддерживаю данный тип сообщений")


async def main() -> None:
    #Объявили бота с токеном c парс модом, который будет форматировать сообщения
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    #Начинаем полинг
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Логирование, оно нужно, чтобы мне не пропустили важные сообщения в консоли
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())