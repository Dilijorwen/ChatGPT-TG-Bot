English description
===================

ChatGPT Telegra Bot
--------------------

This bot was implemented as a freelance project for SmolSchool, now it only supports context-free communication, but you can run it via docker on your own server.
I found the project interesting, as it helped me to remember a little bit the syntax of the language. It was interesting to work with docker, to realise the work of the bot. That's why I think that this project is a good way to start learning programming for schoolchildren.


Full description of the project
-----------------------------------

The bot consists of minimal functions, using the library aiogram, while communication gpt goes through a proxy [from here](https://proxyapi.ru), but if you suddenly need to change to the usual way, it is enough to remove all that is inside OpenAI(). Pictures are generated through this [service](https://www.edenai.co/post/how-to-generate-images-from-text-with-python), and can be changed to the same one we use for gpt.

The bot has commands /help. It will show all the existing commands.
The /dice command will toss a hexagonal die.
The /image {Text} command will generate a picture in the specified promt, but will do it poorly.
Just typing any message will get you a GPT response.

The git.env file has all the project settings. Change the name of the file to ".env"


Technologies
----------------

- Programming Language: Python
- Data storage methods: ".env"
- Project implementation method: The whole project is implemented through aiogram library






Русское описание
===================

ChatGPT Telegra Bot(ru)
--------------------

Этот бот был реализован в качестве фриланс проекта для школы SmolSchool, сейчас он поддерживает только общение без контекста, но запустить его можно через докер на собственном сервере.
Проект мне показался интересным, так как он помог мне немного вспомнить синтаксис языка. Был интересно поработать с докером, реализовать работу бота. Потому считаю, что данный проект, еще и хороший для начала обучения программированию для школьников.


Полное описание проекта(ru)
---------------------------

Бот состоит из минимальных функций, используя библиотеку aiogram, при этом связь gpt идет через прокси [отсюда](https://proxyapi.ru), но если вдруг нужно будет изменить на обычный способ, то, достаточно удалить все, что находится внутри OpenAI(). Картинки генерируются через этот [сервис](https://www.edenai.co/post/how-to-generate-images-from-text-with-python), при этом можно изменить на тот же, что мы используем и для gpt.

У бота есть команды /help. Она покажет все существующие команды.
Команда /dice подбросит шестигранный кубик.
Команда /image {Текст} сгенерирует картинку по-указанному промту, но сделает это плохо.
Просто введя любое сообщение, вам ответит GPT.

В файле git.env есть все настройки проекта. У файла измените название на ".env"


Технологии(ru)
--------------

- Язык программирования: Python
- Методы хранения данных: ".env"
- Метод реализации проекта: Весь проект реализован через библиотеку aiogram








