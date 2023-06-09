from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.environ.get('TOKEN')
bot   = Bot(token=TOKEN) 

btn1 = InlineKeyboardButton(text='admin', url='https://t.me/diyorbekjumanov')
btn2 = InlineKeyboardButton(text='button 2', callback_data='btn2')

inline_keyboard = [
    [btn1, btn2]
]

bot.sendMessage(1258594598, 'salom', reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard))