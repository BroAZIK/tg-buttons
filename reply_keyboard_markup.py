from telegram import Bot, ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.environ.get('TOKEN')
bot   = Bot(token=TOKEN) 

btn1 = KeyboardButton(text='location', request_location=True)
btn2 = KeyboardButton(text='contact', request_contact=True)
btn3 = KeyboardButton(text='hello')

keyboard = [
    [btn1, btn2],
    [btn3]
]

bot.sendMessage(1258594598, 'simple buttons', reply_markup=ReplyKeyboardMarkup(keyboard=keyboard))