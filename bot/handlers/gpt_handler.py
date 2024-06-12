from openai import OpenAI
from dotenv import load_dotenv
from aiogram import Router
from aiogram.types import Message
import os

router = Router()

load_dotenv()

OPENAI_TOKEN = os.environ["OPENAI_TOKEN"]
MODEL_GPT = os.environ["MODEL_GPT"]

client = OpenAI(api_key=f"{OPENAI_TOKEN}",
                base_url="https://api.proxyapi.ru/openai/v1")  # Подключаемся к прокси серверу, для него vpn не надо подключать


def gpt(text):
    # наш знакомый API запрос, только здесь мы не использовали лишних библиотек,
    # openai позаботились о нас и встроили все это в свою библиотеку
    completion = client.chat.completions.create(
        model=f'{MODEL_GPT}',  # Модель можно выбрать на свой вкус
        messages=[
            # Тут задаётся личность нейросети. Настраивается по своему усмотрению (на английском языке)
            {"role": "system", "content": "You are a bot assistant imitating a real person."},
            {'role': 'user', 'content': f'{text}'}  # Запрос от пользователя, который и обрабатывает нейросеть
        ],
        temperature=0.5  # Количество вольности нейросети от 0 до 1. Чем больше, тем больше выразительности и воды
    )

    english_text = completion.choices[0].message.content  # Текст, который он написал

    return english_text


@router.message()  # Любой текст = запрос к chatgpt
async def gpt_handler(message: Message):
    edited = await message.answer('Генерируется ответ♻️')  # Даём понять пользователю, что бот работает
    try:
        await message.reply(gpt(message.text))  # Тут запрос принимается, отдаётся на обработку и выводится
    except Exception as e:
        await message.reply("Мне не удалось ответить на вопрос🥺 Попробуйте позже\n"
                            "Возможные причины: \n"
                            "1) Токен более недействителен\n"
                            "2) У токена закончились деньги\n"
                            "3) Может быть сейчас сервер плохо сработал или не работает прокси")
        print(e) # Если что-то пошло не так, то мы ловим ошибку и выводим в консоль
    await edited.delete()  # Удаляем первое сообщение
