from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    btn1 = InlineKeyboardButton(text='admin', url='https://t.me/jumanovdiyorbek')
    btn2 = InlineKeyboardButton(text='say hello', callback_data='say-hello')

    inline_keyboard = [
        [btn1, btn2]
    ]
    chat_id = update.message.chat.id

    context.bot.sendMessage(
        chat_id, 'Salom, xush kelibsiz!', 
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    )
