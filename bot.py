from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from handlers import (
    start,
    callback_query_handler,
)
import os

TOKEN = os.environ.get('TOKEN')

def main():
    # create updater object
    updater = Updater(token=TOKEN)
    # create dispatcher 
    dispatcher = updater.dispatcher

    # add hendlers
    dispatcher.add_handler(
        handler=CommandHandler(command='start', callback=start)
    )
    dispatcher.add_handler(
        handler=CallbackQueryHandler(callback=callback_query_handler)
    )

    # start polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
