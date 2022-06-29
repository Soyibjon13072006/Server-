import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
wikipedia.set_lang('uz')
API_TOKEN = '5421926371:AAEGia6m_9wRTisdTk9DxUMHOnxTAtL_-8c'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom men malumot bo't man.")

@dp.message_handler()
async def malumot(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    try:
        await message.reply(wikipedia.summary(message.text))
    except:
        await message.reply("Chunmadim")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
