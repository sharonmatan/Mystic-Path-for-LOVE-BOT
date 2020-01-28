import logging
import random

import telegram

import data
import model
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, \
    Filters, Updater, CallbackQueryHandler
import secrets

logging.basicConfig(
    format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    logger.info(f"> Start chat #{chat_id}")
    name = update.effective_user['first_name'].split(" ")[0]
    text = model.get_behind_name(name)
    msg = f"Hello {name} 🌹 \n\nYou have a wonderful name ✨\n\nHere is some info about it:\n\n{text}"
    context.bot.send_message(chat_id=chat_id, text=msg)
    keyboard = [[InlineKeyboardButton("Aries ♈", callback_data='0'),
                 InlineKeyboardButton("Taurus ♉", callback_data='1'),
                 InlineKeyboardButton("Gemini ♊", callback_data='2')],
                [InlineKeyboardButton("Cancer ♋", callback_data='3'),
                 InlineKeyboardButton("Leo ♌", callback_data='4'),
                 InlineKeyboardButton("Virgo ♍", callback_data='5')],
                [InlineKeyboardButton("Libra ♎", callback_data='6'),
                 InlineKeyboardButton("Scorpio ♏", callback_data='7'),
                 InlineKeyboardButton("Sagittarius ♐", callback_data='8')],
                [InlineKeyboardButton("Capricorn ♑", callback_data='9'),
                 InlineKeyboardButton("Aquarius ♒", callback_data='10'),
                 InlineKeyboardButton("Pisces ♓", callback_data='11')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    ms = 'Which Zodiac sign are you?'
    context.job_queue.run_once(one_time_start, when=5, context=[update, context, reply_markup, ms])


def respond(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")
    response = model.get_behind_name(text)
    context.bot.send_message(chat_id=update.message.chat_id, text=response)


def button(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    query = update.callback_query
    msg = f"💖❤💕  LOVE IS IN THE AIR... {chr(9800 + int(query.data))}💋"
    query.edit_message_text(text=msg)
    bio = model.matches_plot(query.data)
    bio.seek(0)
    context.job_queue.run_once(one_time_button, when=5, context=[update, context, chat_id, bio])
    text = """LET'S FIND YOUR LOVER!!!💖\n\n
Choose your favorite path:\n\n /Tarot\n\n           /Stars\n\n                    /Numerology"""
    context.job_queue.run_once(one_time_cards, when=20, context=[update, context, chat_id, text])


def one_time_cards(context: telegram.ext.CallbackContext):
    u = context.job.context[0]
    c = context.job.context[1]
    c_id = context.job.context[2]
    m = context.job.context[3]
    c.bot.send_message(chat_id=c_id, text=m)


def one_time_button(context: telegram.ext.CallbackContext):
    u = context.job.context[0]
    c = context.job.context[1]
    c_id = context.job.context[2]
    b = context.job.context[3]
    c.bot.send_photo(chat_id=c_id, photo=b)


def one_time_start(context: telegram.ext.CallbackContext):
    u = context.job.context[0]
    c = context.job.context[1]
    r_m = context.job.context[2]
    m = context.job.context[3]
    u.message.reply_text(m, reply_markup=r_m)


def cards(update: Update, context: CallbackContext):
    text = update.message.text
    chat_id = update.effective_chat.id
    if text == '/Tarot':
        context.bot.send_photo(chat_id=chat_id, photo=open('tarot.jpg', 'rb'))
        txt = """Tap into the ancient wisdom of the pharoahs to find answers and guidance in your love life with your Egyptian Love Tarot reading.."""
    if text == '/Stars':
        context.bot.send_photo(chat_id=chat_id, photo=open('star_maps.jpg', 'rb'))
        txt = """A birth chart, also known as a natal chart, is a map of where all the major planets and astral bodies were located at the time you were born."""
    if text == '/Numerology':
        context.bot.send_photo(chat_id=chat_id, photo=open('numerology.jpg', 'rb'))
        txt = """In Numerology, each of the nine single digit numbers has a personality"""
    context.bot.send_message(chat_id=chat_id, text=txt)
    when_meet = random.choice(data.TIMES)
    where_meet = random.choice(data.PLACES)
    msg = f"Your personal reading revealed that you have a high potential of meeting someone new this {when_meet} at {where_meet}!\nBest of luck 🌹✨"
    context.job_queue.run_once(one_time_cards, when=10, context=[update, context, chat_id, msg])


def main():
    updater = Updater(token=secrets.BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, respond))
    dispatcher.add_handler(CallbackQueryHandler(button))
    dispatcher.add_handler(CommandHandler('Tarot', cards))
    dispatcher.add_handler(CommandHandler('Stars', cards))
    dispatcher.add_handler(CommandHandler('Numerology', cards))

    logger.info("* Start polling...")
    updater.start_polling()  # Starts polling in a background thread.
    updater.idle()  # Wait until Ctrl+C is pressed
    logger.info("* Bye!")


if __name__ == '__main__':
    main()
