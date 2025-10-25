from telebot import TeleBot
from botlogic import TOKEN
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = TeleBot(TOKEN)

bot.message_handler(commands=['help', 'start', 'lessons', 'motivation'])

# сдесь идут команды бота:

# приветсвие бота.
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,
    """\
    Здравстуй! я бот-расписание.
    Я сдесь чтобы показать нужное тебе расписание занятий.
    Чтобы узнать про все мои команды напишите /help\
    """)

# ответ на команду info
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,
"""
Вот команды, которые могут тебе помочь. их всего то две:
/Info - нужна чтобы вывести список комманд
/Lessons - нужна для выведения расписаний
Удачки в обучении!""")
    
# выдача расписания (мне было лень всё расписывать)
@bot.message_handler(commands=['lessons'])
def lessons(message):
    bot.send_message(message.chat.id,
    ''' вот расписание на эту неделю:
        ======РАСПИСАНИЕ======
    (прим. - перерывы по 10 минут)
    Понедельник:
    1 ур. - Математика (8:00 - 8:40)
    2 ур. - Математика (8:50 - 9:30)
    3 ур. - Английский (9:40 - 10:20)
    4 ур. - Русский (10:30 - 11:10)
    5 ур. - Английский (11:20 - 12:00)
    6 ур. - Физ. культура (12:10 - 12:50)
    
    Вторник:
    .
    .
    .
    .
    .
    .
    
    Среда:
    .
    .
    .
    .
    .
    .
    
    Четверг:
    .
    .
    .
    .
    .
    .
    
    Пятница:
    .
    .
    .
    .
    .
    .
    ''')