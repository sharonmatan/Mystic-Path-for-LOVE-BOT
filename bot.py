import logging
import model
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
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
    msg = f"Hello {name}!\nYou have a wonderful name.  did you know that:\n\n{text}"
    context.bot.send_message(chat_id=chat_id, text=msg)
    keyboard = [[InlineKeyboardButton("Aries ♈", callback_data = '1'),
                InlineKeyboardButton("Taurus ♉", callback_data = '2'),
                InlineKeyboardButton("Gemini ♊", callback_data = '3')],
                [InlineKeyboardButton("Cancer ♋", callback_data = '4'),
                InlineKeyboardButton("Leo ♌", callback_data = '5'),
                InlineKeyboardButton("Virgo ♍", callback_data = '6')],
                [InlineKeyboardButton("Libra ♎", callback_data = '7'),
                InlineKeyboardButton("Scorpio ♏", callback_data = '8'),
                InlineKeyboardButton("Sagittarius ♐", callback_data = '9')],
                [InlineKeyboardButton("Capricorn ♑", callback_data = '10'),
                InlineKeyboardButton("Aquarius ♒", callback_data = '11'),
                InlineKeyboardButton("Pisces ♓", callback_data = '12')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Which sign are you?', reply_markup = reply_markup)
    # context.bot.send_message(chat_id=chat_id, text=f"{text}")


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

