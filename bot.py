import logging
import model
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, \
    Filters, Updater

import secrets

BASE = "https://en.wikipedia.org/wiki/"

logging.basicConfig(
    format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    logger.info(f"> Start chat #{chat_id}")
    name = update.effective_user['first_name']
    print(name)
    text = model.get_behind_name(name)
    context.bot.send_message(chat_id=chat_id, text=f"Hello {name}! you have a wonderful name.. did you know that:")
    context.bot.send_message(chat_id=chat_id, text=f"{text}")


def respond(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    response = model.get_behind_name(text)
    context.bot.send_message(chat_id=update.message.chat_id, text=response)


def main():
    print(secrets.BOT_TOKEN)
    # YOUR BOT HERE
    updater = Updater(token=secrets.BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text, respond)
    dispatcher.add_handler(echo_handler)

    logger.info("* Start polling...")
    updater.start_polling()  # Starts polling in a background thread.
    updater.idle()  # Wait until Ctrl+C is pressed
    logger.info("* Bye!")


if __name__ == '__main__':
    main()

