from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, Defaults
from telegram.ext.dispatcher import run_async

import html
import time
import os
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

defaults = Defaults(parse_mode=ParseMode.HTML, run_async=True)

logger = logging.getLogger(__name__)

special = [ID USER HAS PERMISSION]

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Ciao {update.effective_user.name}\nFai <b>/spengi</b> per ottenere una sorpresa', parse_mode=ParseMode.HTML)

def spengi(update, context):
        keyboard = [
        [
            InlineKeyboardButton("Si", callback_data='yes'),
            InlineKeyboardButton("No", callback_data='no'),
        ]
        ]
        tulipano = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(f'Vuoi spegnere il PC?', reply_markup=tulipano)
        time.sleep(1)
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)

def buttone(update, context):
    query = update.callback_query
    if query.data == 'yes':
        if update.effective_user.id not in special:
            pass
        if update.effective_user.id in special:
            os.system("shutdown /s /t 1")
            context.bot.delete_message(chat_id=update.effective_chat.id, text=f"<b>Ottimo!</b>\n{update.effective_user.name} ha spento il PC con successo", parse_mode=ParseMode.HTML)
    if query.data == 'no':
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.message_id)
        exit()

def main():
  updater = Updater('TOKEN BOTFATHER')
  dispatcher = updater.dispatcher
  ''' BOTTONE'''
  dispatcher.add_handler(CallbackQueryHandler(buttone))
  '''Startazione protonica'''
  dispatcher.add_handler(CommandHandler("start", start))
  dispatcher.add_handler(CommandHandler("spengi", spengi))
  updater.start_polling()
  updater.idle()

if __name__ == '__main__':
    main()
