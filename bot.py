import telegram
from telegram.ext import CommandHandler
from telegram.ext import InlineQueryHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging
import argparse
from telegram.ext import Updater

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
	
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def echo(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
	text_caps = ' '.join(args).upper()
	bot.send_message(chat_id=update.message.chat_id, text=text_caps)

def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)	
	
	
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--bottoken', dest='bottoken', action='store_const')

	args = parser.parse_args()
	updater = Updater(bottoken)
	
	dispatcher = updater.dispatcher
	
	dispatcher.add_handler(CommandHandler('start', start))
	dispatcher.add_handler(MessageHandler(Filters.text, echo))
	dispatcher.add_handler(CommandHandler('caps', caps, pass_args=True))
	dispatcher.add_handler(MessageHandler(Filters.command, unknown))

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    main()
