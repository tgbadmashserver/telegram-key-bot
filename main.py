import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Welcome!\n\nBot setup is successful."
    )

print("✅ Bot Started...")

bot.infinity_polling(skip_pending=True)
