from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
from google_trans_new import google_translator 
import os

BOT_TOKEN = '5462330526:AAHVnNoLYJBULOmDZehUZlP-j5DUybyfwLY'

updater = Updater(BOT_TOKEN,use_context = True )

def start(updater,context):
 updater.message.reply_text('hi i am google translater')
 
def echo(updater,context):
 usr_msg =updater.message.text
 translator=google_translator()
 translate_text=translator.translate(usr_msg,lang_tgt='ml')
 updater.message.reply_text(translate_text)
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
