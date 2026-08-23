import os
import telebot

TOKEN = os.environ["BOT_TOKEN"]

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
