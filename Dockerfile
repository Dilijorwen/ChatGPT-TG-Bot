# Это мы скачиваем python 3.12 в наш контейнер
FROM python:3.12
# У казываем нашу рабочую дирикторию для уда будет скачиваться наш проетк
WORKDIR /app

# Из проекта скачиваем requirements и сохраняем его под тем же названием
COPY requirements.txt requirements.txt

# обновляем примочки пространства
RUN pip install --upgrade setuptools

# Скачиваем  все библиотеки из requirements
RUN pip install -r requirements.txt

# Устанавливаем уровень доступа, у нас, как у создателя полные прfва,
# а если дадим доступ к контейнеру другому, то он сможет только запустить и прочекать docker
RUN chmod 755 .

# копируем весь на проект
COPY . .

# запус проекта
CMD ["python", "bot/telegram.py"]