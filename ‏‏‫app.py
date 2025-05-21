from flask import Flask, request
import os
import telegram

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")

bot = telegram.Bot(token=BOT_TOKEN)

@app.route(f"/webhook/{WEBHOOK_SECRET}", methods=["POST"])
def webhook():
    if request.headers.get('X-Telegram-Bot-Api-Secret-Token') != WEBHOOK_SECRET:
        return "unauthorized", 403

    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.effective_chat.id
    message = update.message.text

    if message == "/start":
        bot.send_message(chat_id=chat_id, text="✨ שלום! OptiBot כאן בשבילך. נתחיל?")
    else:
        bot.send_message(chat_id=chat_id, text=f"📩 קיבלתי: {message}")

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
