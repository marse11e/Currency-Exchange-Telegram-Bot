# Currency Exchange Telegram Bot

## Описание проекта

Этот проект представляет собой Django-приложение, созданное для работы с телеграм-ботом, предназначенным для обмена валют и конвертации единиц измерения диапазона.

```bash
# Установка
git clone git@github.com:marse11e/Currency-Exchange-Telegram-Bot.git
cd Currency-Exchange-Telegram-Bot
python3 -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
echo "TELEGRAM_BOT_TOKEN=ваш_токен_телеграм_бота" > .env

# Запуск
python3 manage.py runserver
python3 manage.py runbot
```

# Использование
1. Добавьте вашего бота в Телеграме и начните диалог, введя команду `/start`.
2. Для обмена валют бот предложит вам ввести сумму, выбрать исходную и целевую валюты.
3. Для конвертации единиц измерения диапазона бот запросит у вас значение, исходную и целевую единицы измерения.

# Лицензия
Этот проект распространяется под лицензией MIT. Подробности см. в файле [LICENSE](LICENSE).

# Автор
marse11e - marselle.naz@yandex.kz