import os
import time
import threading
import json
import requests

# Импорты для Telegram-бота
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Импорты для Flask
from flask import Flask, render_template_string

# ================== КОНФИГУРАЦИЯ ==================
TOKEN = os.environ.get("TOKEN")  # или впиши сюда свой токен вручную
if not TOKEN:
    print("❌ Ошибка: токен не найден! Укажи его в переменной окружения TOKEN или в коде.")
    exit(1)

# ================== TELEGRAM БОТ ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я работаю!")

def run_bot():
    """Запускает Telegram-бота в отдельном потоке"""
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Бот запущен и слушает команды...")
    app.run_polling()

# ================== FLASK (для keep-alive) ==================
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    # Простая страничка, чтобы Render видел, что приложение живо
    html = '''
    <center>
        <h1>Бот работает!</h1>
        <img src="https://i.giphy.com/media/3o7abAHdX5Yr4/320i.gif" />
    </center>
    '''
    return html

@app_flask.route('/ping')
def ping():
    # Эндпоинт для cron-job.org
    return "pong", 200

def run_flask():
    """Запускает Flask-сервер на порту 10000 (как требует Render)"""
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

# ================== ЗАПУСК ВСЕГО ==================
if __name__ == "__main__":
    # Запускаем бота в отдельном потоке, чтобы Flask не блокировал
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # Запускаем Flask в основном потоке
    run_flask()
flask
python-telegram-bot
requests
