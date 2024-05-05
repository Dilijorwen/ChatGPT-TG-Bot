from aiogram import Router, html
from aiogram.filters.command import CommandStart
from aiogram.types import Message

# Объявляем роутер для декоратора
router = Router()

@router.message(CommandStart()) #Вот так выглядит декоратор для роутера
# Мы можем записать его так:@router.message(Command("start"))
# Хэндлер для команды /start
async def command_start_handler(message: Message) -> None:
    # await - требование к вызову функции для асинхронки
    # После messeage стоит дополнение к функции, которое говорит, что бот сделает
    # massage.from_user.full_name - Определяет имя пользователья
    # html.bold - делает жирную разметку для имени пользователя в стиле html(для этого мы ниже делам parse_mode)
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}! \nНапиши /help")
