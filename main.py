import os
import threading
import time

from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")
if not TOKEN:
    print("❌ Токен не найден. Добавь переменную окружения TOKEN.")
    exit(1)

# ==================== TELEGRAM BOT ====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Бот работает!")

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Бот запущен...")
    app.run_polling()

# ==================== FLASK ====================
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Бот работает!"

@flask_app.route('/ping')
def ping():
    return "pong", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)

# ==================== ЗАПУСК ====================
if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    run_flask()
