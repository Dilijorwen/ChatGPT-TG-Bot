import json
import os

import requests
from dotenv import load_dotenv

from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message, FSInputFile

router = Router()

load_dotenv()

IMAGEAI_TOKEN = os.environ["IMAGEAI_TOKEN"]
URL_IMAGEAI = os.environ["URL_IMAGEAI"]
MODEL_IMAGEAI = os.environ["MODEL_IMAGEAI"]
RESOLUTION_IMAGEAI = os.environ["RESOLUTION_IMAGEAI"]
STYLE_IMAGEAI = os.environ["STYLE_IMAGEAI"]


def text_to_image(text: str, id: int):
    # Это и есть общение с API
    # Здесь даем ему наш токен в header, мы его не разбирали, но он похож на body
    headers = {
        "Authorization": f"Bearer {IMAGEAI_TOKEN}"}

    # Ссылка API
    url = f"{URL_IMAGEAI}"

    # Наш body
    payload = {
        "providers": f"{MODEL_IMAGEAI}",
        "text": f"{text}",
        # Это наш промт, то есть текст, по которому мы получим котенку. Его мы передаем в саму функцию
        f"{MODEL_IMAGEAI}": f"{STYLE_IMAGEAI}",
        "resolution": f"{RESOLUTION_IMAGEAI}",
    }

    # Получаем ответ на наш пост запрос
    # request.post - это пост запрос по нашему API, мы отправляем ему body(payload) и headers
    response = requests.post(url, json=payload, headers=headers)
    # Мы получили на ша ответ в json формате, то есть в формате словаря
    result = json.loads(response.text)

    # Это мы получаем нужныем нам данные, то есть ссылку на картинку
    image_url = result[f'{MODEL_IMAGEAI}']['items'][0]['image_resource_url']
    r = requests.get(image_url)

    # Насильно создаст папку images в директории с ботом, нужно для docker
    os.makedirs("images", exist_ok=True)

    # Cохранит картинку в нужную папку
    with open(f'images/{id}.png', 'wb') as file:
        file.write(r.content)


@router.message(Command("image"))
async def command_image_handler(message: Message):
    # Сохраняем сообщение, чтобы его потом удалить
    # Я не знаю как точно это работает,
    # но скорее всего он сохраняет id сообщения и чата в эту переменную
    edited = await message.reply('Генерируется картинка️️🏞')

    # Мы пишем ему /image {текст},
    # эта строка убирает image и оставляет текст
    # Бот не видит этот "/", он нужен для активации команды
    text = message.text[6:]

    # Сохраняем  id для нейминга файла
    id = message.chat.id

    # Вызываем функцию
    text_to_image(text, id)

    try:
        await message.reply_photo(photo=FSInputFile(f"images/{id}.png"))
        # Ловит все ошибки
        # Так нельзя, лучше ловить все ошибки отдельными ошибками,
        # чтобы пользователь понимал точно в чем ошибка
        # ы ее сохраняем как переменную "e"
    except Exception as e:
        await message.reply("Мне не удалось ответить на вопрос🥺Попробуйте позже\n"
                            "Возможные причины: \n"
                            "1) Токен более недействителен\n"
                            "2) У токена закончились деньги\n"
                            "3) Может быть сервер плохо сработал")
        print(e)  # Выводим ошибку в консоль для понимания, что случилось, чтобы исправить
    await edited.delete()
