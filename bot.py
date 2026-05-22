import telebot
import requests
from WebCalcTrackbot.config import BOT_TOKEN
import WebCalcTrackbot.database as database
import os
from dotenv import load_dotenv
load_dotenv()


bot = telebot.TeleBot(token=os.getenv("BOT_TOKEN"))

# При запуске бота проверяем, создана ли таблица
database.create_table()

# Список разрешенных валют (как ты просил)
ALLOWED_CURRENCIES = ["USD", "EUR", "JPY", "GBP", "CNY", "CHF", "AUD", "CAD", "HKD", "SGD", "MXN", "INR", "KRW", "NZD", "NOK", "SEK", "DKK", "PLN", "ZAR", "THB", "BRL", "CZK", "AED", "SAR", "TRY", "IDR", "MYR", "PHP", "CLP", "RON", "AMD", "RUB", "GEL"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши сумму и валюты. Пример: 100 USD EUR")

@bot.message_handler(func=lambda m: True)
def convert(message):
    try:
        # Разделяем сообщение пользователя (например: "100", "USD", "EUR")
        parts = message.text.upper().split()
        amount = float(parts[0])
        from_curr = parts[1]
        to_curr = parts[2]

        if from_curr not in ALLOWED_CURRENCIES or to_curr not in ALLOWED_CURRENCIES:
            bot.reply_to(message, "Я не знаю такую валюту. Проверь список!")
            return

        # Узнаем курс валют через бесплатный сайт (API)
        url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
        response = requests.get(url).json()
        rate = response['rates'].get(to_curr)

        if rate:
            result = amount * rate
            bot.reply_to(message, f"{amount} {from_curr} = {result:.2f} {to_curr}")
            
            # Сохраняем в базу данных
            user_id = str(message.from_user.id)
            username = message.from_user.username or "Без имени"
            database.add_log(user_id, username, from_curr, to_curr, amount, result)
        else:
            bot.reply_to(message, "Сбой получения курса валют.")

    except Exception as e:
        bot.reply_to(message, "Ошибка! Пиши строго по примеру: 100 USD EUR")

if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)