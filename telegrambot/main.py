import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5864572830:AAG8-Nw65fvnK2sqKQVoWH-C3BQAKP0Tx3c'
wikipedia.set_lang("uz")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


#1-handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Assalom aleykum wikipedia botiga xush kelibsiz!")


#2-handler
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):

    await message.answer("Bu bot sizga ma'lumot topishga yordam beradi")


#3-handler
@dp.message_handler()
async def echo(message: types.Message):
    savol = message.text
    try:
        javob = wikipedia.summary(savol)
        await message.answer(javob)
    except:
        await message.answer("Bu mauvzuga oid ma'lumot topolmadi !")
    
Dispatcher.poll_handler(CommandHandler('start', start)) 
Dispatcher.poll_handler(CommandHandler('help', help))



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)