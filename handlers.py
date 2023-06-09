from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    btn1 = InlineKeyboardButton(text='admin', url='https://t.me/jumanovdiyorbek')
    btn2 = InlineKeyboardButton(text='say hello', callback_data='say-hello')
    btn3 = InlineKeyboardButton(text='say hi', callback_data='say-hi')

    inline_keyboard = [
        [btn3, btn2],
        [btn1]
    ]
    chat_id = update.message.chat.id

    context.bot.sendMessage(
        chat_id, 'Salom, xush kelibsiz!', 
        reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    )

def callback_query_handler(update: Update, context: CallbackContext):
    callback_query = update.callback_query

    if callback_query.data == 'say-hello':
        update.callback_query.message.reply_text(f'Hello')
        
    if callback_query.data == 'say-hi':
        update.callback_query.message.reply_text(f'Hi')