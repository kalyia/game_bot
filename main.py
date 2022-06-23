import telebot

token = "5299505355:AAGv8lg9W-Udjrlya6lk8X6l9saWKkX9o-w"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'hi'])
def start_message(message):
  bot.send_message(message.chat.id, "Hello, I am bot!")

@bot.message_handler(content_types=['sticker'])
def send_sticker_on_sticker(message):
  bot.send_sticker(message.chat.id, message.sticker.file_id)

bot.polling()
