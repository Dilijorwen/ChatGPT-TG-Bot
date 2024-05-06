from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.enums.dice_emoji import DiceEmoji

router = Router()

@router.message(Command("dice"))
async def command_dice_handler(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)