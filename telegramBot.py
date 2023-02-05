'''
Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале.
Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой.
В конце вывести игрока, который победил

Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.
 Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
 Все конфеты оппонента достаются сделавшему последний ход.

В качестве дополнительного усложнения можно:
a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм,
позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить,
соответственно внедрить этот алгоритм боту )
'''

import telebot
from telebot import types
import random


bot = telebot.TeleBot("5911932496:AAHGeapoQveYTYXt2Z4SH6_0Lf8ymexERJ8")

sweets = 221
max_sweet = 28

flag = None


@bot.message_handler(commands = ['start'])  # вызов функции по команде в списке
def start(message):
    global flag
    bot.send_message(message.chat.id, f"Welcome to my game!")
    flag = random.choice(['user', 'bot'])
    bot.send_message(message.chat.id, f'Overall, there are {sweets} sweets')
    if flag == 'user':
        bot.send_message(message.chat.id, "It's your first turn")
    else:
        bot.send_message(message.chat.id, "First turn for bot")

    controller(message)

def controller(message):
    global flag
    if sweets > 0:
        if flag == 'user':
            bot.send_message(message.chat.id, f"Your turn. Choose a number from 0 to {max_sweet}")
            bot.register_next_step_handler(message, user_input)
        else:
            bot_input(message)

    else:
        flag = 'user' if flag == 'bot' else 'bot'
        bot.send_message(message.chat.id, f'The winner is {flag}')

def bot_input(message):
    global flag, sweets
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet - 1
    else:
        bot_turn = sweets % max_sweet - 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f'The bot took {bot_turn} sweets')
    bot.send_message(message.chat.id, f'There are {sweets} sweets left')
    flag = 'user' if flag == 'bot' else 'bot'

    controller(message)

def user_input(message):
    global sweets, flag
    user_turn = int(message.text)
    if user_turn > 28 or user_turn < 0:
        bot.send_message(message.chat.id, 'You have choose a wrong number!')

    else:
        sweets -= user_turn
        bot.send_message(message.chat.id, f'There are {sweets} sweets left')
        flag = 'user' if flag == 'bot' else 'bot'

    controller(message)













'''
    def summa(message):

    summ = sum(list(map(int, message.text.split())))
    bot.send_message(message.chat.id, str(summ))
    button(message)

def difference(message):
    sets = list(map(int, message.text.split()))
    diff = sets[0] - sets[1]
    bot.send_message(message.chat.id, str(diff))
    button(message)

@bot.message_handler(commands=["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание клавиатуры
    but1 = types.KeyboardButton("Sum")  # создание кнопок
    but2 = types.KeyboardButton("Difference")
    markup.add(but1) # добавление кнопок
    markup.add(but2) # добавление кнопок
    bot.send_message(message.chat.id, "Choose below", reply_markup=markup)

@bot.message_handler(content_types=["text"]) # вызов функции если тип сообщения - текст
def controller(message):
    if message.text == "Sum":
        bot.send_message(message.chat.id,"choose two numbers for sum")
        bot.register_next_step_handler(message, summa) # вызов функции на ответ пользователя
    elif message.text == "Difference":
        bot.send_message(message.chat.id,"choose two numbers for difference")
        bot.register_next_step_handler(message, difference)

'''

bot.infinity_polling()

