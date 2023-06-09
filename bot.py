from telegram.ext import Updater, CommandHandler
from handlers import (
    start,
)
import os

TOKEN = os.environ.get('TOKEN')

def main():
    # create updater object
    updater = Updater(token=TOKEN)
    # create dispatcher 
    dispatcher = updater.dispatcher

    # add hendlers
    dispatcher.add_handler(handler=CommandHandler(command='start', callback=start))

    # start polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
