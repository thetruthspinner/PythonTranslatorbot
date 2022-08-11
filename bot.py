from telegram.ext import Updater,MessageHandler,CommandHandler,Filters
#from google_trans_new import google_translator 
from googletrans import Translator
import os
import requests

BOT_TOKEN = '5462330526:AAHVnNoLYJBULOmDZehUZlP-j5DUybyfwLY'

updater = Updater(BOT_TOKEN,use_context = True )

def start(updater,context):
 updater.message.reply_text('hi i am google translater')
 
def echo(updater,context):
 updater.message.reply_text('Working function')
 usr_msg = updater.message.text
 context.bot.send_message(updater.message.chat.id, usr_msg)
 translator = Translator(service_urls=['translate.googleapis.com'])  
 translation = translator.translate(usr_msg,dest='hi')
 x= translation.text
 context.bot.send_message("@Python_Translatorbot", x)
 updater.message.reply_text('function reached here')
 
 
dp =updater.dispatcher.add_handler
dp(CommandHandler('start',start))
dp(MessageHandler(Filters.text,echo))

updater.start_polling()
updater.idle()
