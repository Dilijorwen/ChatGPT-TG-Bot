from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

router = Router()

@router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    await message.reply("Привет! Я тестовый бот для методички\n"
                         "У менять есть селудующие команды:\n"
                        "/dice - мы с тобой кинем шестигранный кубик\n"
                        "/help - выведу тебе данное сообщение\n"
                        "/image - создам изображение по запросу (например, /image кошка).\n"
                        "Или ты можешь ввести просто сообщение и тебе ответит GPT")