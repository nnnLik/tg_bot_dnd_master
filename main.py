from aiogram import (Bot, Dispatcher,
                     executor, types)

from os import getenv
from sys import exit

import logging
import config

# Bot object
bot = Bot(token=config.Token, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


#const var
Greating = '''
Hi
'''


@dp.message_handler(commands="start")
async def cmd_test1(message: types.Message):

    buttons = ["Handbook",
               "Create Hero",
               "Generate Loot",
               "Generate Mobs",
               "Music"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer(Greating, reply_markup=keyboard)






@dp.message_handler(commands="dice")
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)