import logging
from aiogram import Bot, Dispatcher, executor, types

import config

# Bot object
bot = Bot(token=config.Token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

if not config.Token:
    exit("Error: no token provided")

@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):
    await message.answer("Test")

@dp.message_handler(commands="dice")
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)