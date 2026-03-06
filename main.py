import telebot
import os
from flask import Flask

# আপনার টোকেন
API_TOKEN = '8712770894:AAE3NkNg4_OGiw4q3MjpODFaroud1jMM0MA'
bot = telebot.TeleBot(API_TOKEN)

# Render-এর জন্য একটি ছোট সার্ভার (যাতে বট বন্ধ না হয়)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ANIMAX WORLD বট এখন Render-এ লাইভ আছে!")

@bot.message_handler(content_types=['video'])
def handle_video(message):
    file_id = message.video.file_id
    file_info = bot.get_file(file_id)
    video_url = f"https://api.telegram.org/file/bot{API_TOKEN}/{file_info.file_path}"
    bot.reply_to(message, f"আপনার ভিডিও লিঙ্ক:\n{video_url}")

@server.route("/")
def webhook():
    return "Bot is Running", 200

if __name__ == "__main__":
    # বট একসাথে চালানো
    import threading
    threading.Thread(target=bot.polling, daemon=True).start()
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

