import logging

import requests
import telebot
from telebot import types

from django.conf import settings
from django.core.files.base import ContentFile

from .models import TelegramUser
from .button import main, currency, unit_of_measurement, crypto_currency
from .pars import Parser


bot = telebot.TeleBot(settings.TOKEN_BOT, parse_mode="HTML")


def ads(ads_telegram):
    users = TelegramUser.objects.all()
    for user in users:
        print("ads")
        text = ads_telegram.text 
        if ads_telegram.url:
            text += f"\n\n<a href='{ads_telegram.url}'>{ads_telegram.url.split('/')[2].split('.')[0]}</a>"

        if ads_telegram.url2:
            text += f"\n\n<a href='{ads_telegram.url2}'>{ads_telegram.url2.split('/')[2].split('.')[0]}</a>"

        if ads_telegram.image:
            with open(ads_telegram.image.path, "rb") as f:
                bot.send_photo(user.user_id, f, caption=text)
        else:
            bot.send_message(user.user_id, text)
    return


class TelegramAvatar:
    def __init__(self, message, model_user):
        self.user_id = message.from_user.id
        self.model_user = model_user
        
    def get_avatar(self):
        photos = bot.get_user_profile_photos(self.user_id, limit=1)
        if photos.photos:
            file_id = photos.photos[0][-1].file_id
            file_info = bot.get_file(file_id)
            file_url = settings.GET_FILE_URL + file_info.file_path
            response = requests.get(file_url)
            if response.status_code == 200:
                self.model_user.image.save(f"{self.model_user.user_id}_profile_photo.jpg", ContentFile(response.content), save=True)
            return
        
        response = requests.get(settings.DEFULT_IMAGE)
        if response.status_code == 200:
            self.model_user.image.save(f"{self.model_user.user_id}_profile_photo.jpg", ContentFile(response.content), save=True)
            return
        
        return None

@bot.message_handler(commands=['start'])
def start(message):
    # извлекаем данные пользователя из объекта message
    from_user = message.from_user

    model_user, created = TelegramUser.objects.get_or_create(user_id=from_user.id)

    if created:
        model_user.user_id = from_user.id
        model_user.username = from_user.username
        model_user.first_name = from_user.first_name
        model_user.last_name = from_user.last_name
        model_user.language_code = from_user.language_code
        model_user.is_bot = from_user.is_bot
        model_user.save()

        TelegramAvatar(message, model_user).get_avatar()

    bot.send_message(
        message.chat.id, 
        f"Добро пожаловать {model_user.get_name()} в наш бот для обмена валют! Я могу помочь вам конвертировать валюты по текущему курсу.", 
        reply_markup=main()
    )


@bot.message_handler(func=lambda message: message.text.lower() == "меню")
def menu(message):
    bot.send_message( message.chat.id,  "Выберите нужную опцию:",  reply_markup=main())


def currency_convert_step_two(message, url):
    try:
        amount = float(message.text)
        rezult = Parser(url + str(amount))
    except:
        bot.send_message( message.chat.id, "Неверный ввод. Попробуйте еще раз.")
        bot.register_next_step_handler(message, currency_convert_step_two, url)
    
    else:
        bot.send_message( message.chat.id, f"Результат: {rezult.proccessing_method()}", reply_markup=main())
        return

def currency_convert_step(message):
    if message.text.lower() in settings.CONVERT:
        bot.send_message( message.chat.id,  "Напиши сумму для конвертации:",  reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, currency_convert_step_two, settings.CONVERT[message.text.lower()])
        return
    else:
        bot.send_message( message.chat.id, "Неверный ввод.", reply_markup=main())
        return
        

@bot.message_handler(func=lambda message: message.text.lower() == "конвертация валюты")
def currency_convert(message):
    bot.send_message( message.chat.id,  "Выберите нужную опцию:",  reply_markup=currency(settings.CONVERT))
    bot.register_next_step_handler(message, currency_convert_step)


def crypto_convert_step_two(message, url):
    try:
        amount = float(message.text)
        rezult = Parser(url + str(amount))
    except:
        bot.send_message( message.chat.id, "Неверный ввод. Попробуйте еще раз.")
        bot.register_next_step_handler(message, crypto_convert_step_two, url)
    
    else:
        bot.send_message( message.chat.id, f"Результат: {rezult.proccessing_method()}", reply_markup=main())
        return


def crypto_convert_step(message):
    if message.text.lower() in settings.CRYPTHO_CONVERT:
        bot.send_message( message.chat.id,  "Напиши сумму для конвертации:",  reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, crypto_convert_step_two, settings.CRYPTHO_CONVERT[message.text.lower()])
        return
    else:
        bot.send_message( message.chat.id, "Неверный ввод.", reply_markup=main())
        return


@bot.message_handler(func=lambda message: message.text.lower() == "конвертация крипты")
def crypto(message):
    bot.send_message( message.chat.id,  "Выберите нужную опцию:",  reply_markup=crypto_currency(settings.CRYPTHO_CONVERT))
    bot.register_next_step_handler(message, crypto_convert_step)



@bot.message_handler(func=lambda message: message.text == "Профиль")
def profile(message):
    from_user = message.from_user
    model_user = TelegramUser.objects.get(user_id=from_user.id)
    if not model_user.image:
        TelegramAvatar(message, model_user).get_avatar()
    text = ( f"🪪Уважаемый(ая) {model_user.get_full_name()}\n" f"🪪Имя: {model_user.first_name}\n" f"🪪Фамилия: {model_user.last_name}\n" f"🪪Имя поль-ля: {model_user.username}\n" f"📅Дата регистрации: {model_user.created_at.strftime('%d.%m.%Y')}\n")
    bot.send_photo(message.chat.id, photo=model_user.image, caption=text, has_spoiler=True)


def measurement_3(message, iz):
    if str(message.text).isdigit():
        if iz == 1:
            text = (
                f"Километр (км) - {message.text} км = {int(message.text) * 1000} м\n"
                f"Километр (км) - {message.text} км = {int(message.text) * 100000} дм\n"
                f"Километр (км) - {message.text} км = {int(message.text) * 1000000} см\n"
                f"Километр (км) - {message.text} км = {int(message.text) * 10000000} мм\n"
            )
            bot.send_message( message.chat.id, text, reply_markup=main())
            return
        
        elif iz == 2:
            text = (
                f"Метр (м) - {message.text} м = {int(message.text) / 1000} км\n"
                f"Метр (м) - {message.text} м = {int(message.text) * 10} дм\n"
                f"Метр (м) - {message.text} м = {int(message.text) * 100} см\n"
                f"Метр (м) - {message.text} м = {int(message.text) * 1000} мм\n"
            )
            bot.send_message( message.chat.id, text, reply_markup=main())
            return

        elif iz == 3:
            text = (
                f"Сантиметр (см) - {message.text} см = {int(message.text) / 100000} км\n"
                f"Сантиметр (см) - {message.text} см = {int(message.text) / 100} м\n"
                f"Сантиметр (см) - {message.text} см = {int(message.text) / 10} дм\n"
                f"Сантиметр (см) - {message.text} см = {int(message.text) * 10} мм\n"
            )
            bot.send_message( message.chat.id, text, reply_markup=main())
            return

        elif iz == 4:
            text = (
                f"Дециметр (дм) - {message.text} дм = {int(message.text) / 10000} км\n"
                f"Дециметр (дм) - {message.text} дм = {int(message.text) / 10} м\n"
                f"Дециметр (дм) - {message.text} дм = {int(message.text) * 10} см\n"
                f"Дециметр (дм) - {message.text} дм = {int(message.text) * 100} мм\n"
            )
            bot.send_message( message.chat.id, text, reply_markup=main())
            return
        
        elif iz == 5:
            text = (
                f"Миллиметр (мм) - {message.text} мм = {int(message.text) / 1000000} км\n"
                f"Миллиметр (мм) - {message.text} мм = {int(message.text) / 1000} м\n"
                f"Миллиметр (мм) - {message.text} мм = {int(message.text) / 100} дм\n"
                f"Миллиметр (мм) - {message.text} мм = {int(message.text) / 10} см\n"
            )
            bot.send_message( message.chat.id, text, reply_markup=main())
            return

        else:
            bot.send_message( message.chat.id, "Что-то пошло не так.")
            
    else:
        bot.send_message( message.chat.id, "Неверный ввод. Попробуйте еще раз.")
        bot.register_next_step_handler(message, measurement_3, iz)


def measurement_2(message):
    ms = str(message.text)
    if ms.startswith("Километр"):
        bot.send_message(message.chat.id, "Введите сумму для измерения:", reply_markup=main())
        bot.register_next_step_handler(message, measurement_3, 1)
        return
    
    elif ms.startswith("Метр"):
        bot.send_message(message.chat.id, "Введите сумму для измерения:", reply_markup=main())
        bot.register_next_step_handler(message, measurement_3, 2)
        return

    elif ms.startswith("Сантиметр"):
        bot.send_message(message.chat.id, "Введите сумму для измерения:",reply_markup=main())
        bot.register_next_step_handler(message, measurement_3, 3)
        return
    
    elif ms.startswith("Дециметр"):
        bot.send_message(message.chat.id, "Введите сумму для измерения:",reply_markup=main())
        bot.register_next_step_handler(message, measurement_3, 4)
        return
    
    elif ms.startswith("Миллиметр"):
        bot.send_message(message.chat.id, "Введите сумму для измерения:",reply_markup=main())
        bot.register_next_step_handler(message, measurement_3, 5)
        return

    else:
        bot.send_message( message.chat.id, "Неверный ввод.", reply_markup=main())
        return


@bot.message_handler(func=lambda message: message.text.lower() == "конвертация единиц измерения")
def measurement(message):
    text = (
        "Километр (км) - 1 км = 1000 метров\n"
        "Метр (м) - 1 м = 100 сантиметров.\n"
        "Сантиметр (см) - 1 см = 10 миллиметров.\n"
        "Дециметр (дм) - 1 дм = 10 сантиметров.\n"
        "Миллиметр (мм).\n\n"
        "Выберите нужную опцию:"
    )
    bot.send_message(message.chat.id,  text,  reply_markup=unit_of_measurement())
    bot.register_next_step_handler(message, measurement_2)


def RunBot():
    print("Началась процедура операция [ Ы ]")
    bot.polling(none_stop=True, interval=0)
    