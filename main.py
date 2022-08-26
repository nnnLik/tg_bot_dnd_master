from aiogram import (Bot, Dispatcher,
                     executor, types)

from os import getenv
from sys import exit

import logging
import config

# Bot object
Bot = Bot(token=config.Token, parse_mode=types.ParseMode.HTML)

Dispatcher_bot = Dispatcher(Bot)
logging.basicConfig(level=logging.INFO)


#const var
Greating = '''
Hi
'''


@Dispatcher_bot.message_handler(commands="start")
async def main_menu(message: types.Message):

    buttons = ["Handbook",
               "Create Hero",
               "Generate Loot",
               "Generate Mobs",
               "Music"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer(Greating, reply_markup=keyboard)

@Dispatcher_bot.message_handler(lambda message: message.text == "Handbook")
async def handbook(message: types.Message):

    buttons = ["Movement/Action",
               "State",
               "Damage",
               "Weapon",
               "Other",
               "Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer("Here you can find all the <b>basic information</b>, which has been divided into parts for your convenience.", reply_markup=keyboard)



# Return to main menu
@Dispatcher_bot.message_handler(lambda message: message.text == "Back to Menu")
async def back_menu(message: types.Message):

    buttons = ["Handbook",
               "Create Hero",
               "Generate Loot",
               "Generate Mobs",
               "Music"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer('<b>Whoo</b>', reply_markup=keyboard)


# @dp.message_handler(commands="dice")
# async def cmd_dice(message: types.Message):
#     await message.answer_dice(emoji="🎲")

if __name__ == "__main__":
    executor.start_polling(Dispatcher_bot, skip_updates=True)