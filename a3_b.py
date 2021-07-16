from telegram.ext import Updater, CommandHandler

#handler, se ejecuta con accion de usuario
def start(update, context):

    update.message.reply_text('Hello, world c:')


if __name__ == '__main__':

    #Updater, peticiones que se reciben, usuarios pet
    updater = Updater(token='1888150684:AAFmur6f8YSjbzAOP72bDf-_2-oAtF-r6NY', use_context=True)
    #enviar las acciones, manejo de comandos
    dp = updater.dispatcher

    #vincular el handler (start) con el dispatcher
    dp.add_handler(CommandHandler('start',start))

    #add handler
    #sp de comandos continuo, bucle
    updater.start_polling()
    updater.idle()