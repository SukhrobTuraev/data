import telegram.ext

Token = '5778083987:AAG-UU12QTg8o7D-IExZi_eZO2BqSQwZWtI'
updater = telegram.ext.updater('5778083987:AAG-UU12QTg8o7D-IExZi_eZO2BqSQwZWtI', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
  update.message.reply_text("Hello Welcome to Bot")

def help(update, context):
  update.message.reply_text(
    """
    /start -> Welcome to channel
    /help -> This praticular message
    /context -> About various Playlists of Bot 
    /Python -> The first video from Python playlist
    """
  )

  def content(update, context):
    update.message.reply_text(" We have various playlists and articles available")


  def Python(update, context):
    update.message.reply_text("link : https://youtu.be/227uk4kDTM8")   

dispatcher.add_handler(telegram.ext.CommandHandler('start', start)) 
dispatcher.add_handler(telegram.ext.CommandHandler('Pyhton', Python)) 
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))

updater.start_polling()
updater.idle()
