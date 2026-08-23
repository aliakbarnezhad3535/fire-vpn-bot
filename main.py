import os
import telebot

TOKEN = os.environ["8866454964:AAE3Q2h-2gkbpjSzbOH35ryEEdSTDPfHAjo"]

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "سلام 👋\n"
        "به ربات Fire VPN خوش اومدی 🔥\n\n"
        "🛒 خرید کانفیگ\n"
        "💰 تعرفه‌ها\n"
        "📞 پشتیبانی"
    )

bot.infinity_polling()
