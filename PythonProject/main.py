import telebot
# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = '7567816356:AAFaUrQ0zD0VzQmW44C2_I8PGy7XRX7xBXE'
bot = telebot.TeleBot(TOKEN)

  # Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может выполнять   несколько команд. Используйте /help для подробностей.")

  # Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
      help_text = (
          "/start - Начать диалог с ботом\n"
          "/help - Показать это сообщение\n"
          "/perevorot <текст> - Перевернуть введённый текст\n"
          "/caps <текст> - Преобразовать текст в заглавные буквы\n"
          "/cut <текст> - Удалить все гласные из текста"
      )
      bot.send_message(message.chat.id, help_text)

  # Обработчик команды /perevorot
@bot.message_handler(commands=['perevorot'])
def handle_perevorot(message):
      text_to_reverse = message.text[len('/perevorot '):]
      reversed_text = text_to_reverse[::-1]
      bot.send_message(message.chat.id, reversed_text)

  # Обработчик команды /caps
@bot.message_handler(commands=['caps'])
def handle_caps(message):
      text_to_caps = message.text[len('/caps '):]
      caps_text = text_to_caps.upper()
      bot.send_message(message.chat.id, caps_text)

  # Обработчик команды /cut
@bot.message_handler(commands=['cut'])
def handle_cut(message):
      text_to_cut = message.text[len('/cut '):]
      vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"
      cut_text = ''.join([char for char in text_to_cut if char not in vowels])
      bot.send_message(message.chat.id, cut_text)

  # Запуск бота
bot.polling(none_stop=True)