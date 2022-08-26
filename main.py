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


# Main menu
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


# HandBook
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

    await message.answer("Here you can find all the <b>basic information</b>, which has been divided into parts for your convenience.",
                         reply_markup=keyboard)

# HandBook -> Movement/Action
@Dispatcher_bot.message_handler(lambda message: message.text == "Movement/Action")
async def handbook(message: types.Message):

    buttons = ["Movement",
               "Action",
               "Bonus Action",
               "Reactions",
               "Free actions",
               "Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.reply("Choose the option that interests you",
                         reply_markup=keyboard)

# HandBook -> State
@Dispatcher_bot.message_handler(lambda message: message.text == "State")
async def handbook(message: types.Message):

    buttons = ["State",
               "Environment and Perception",
               "Hits, Death, and Rest",
               "Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.reply("Choose the option that interests you",
                         reply_markup=keyboard)

# HandBook -> Damage
@Dispatcher_bot.message_handler(lambda message: message.text == "Damage")
async def handbook(message: types.Message):

    buttons = ["Damage and Attacks",
               "Spells",
               "Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.reply("Choose the option that interests you",
                         reply_markup=keyboard)

# HandBook -> Weapon
@Dispatcher_bot.message_handler(lambda message: message.text == "Weapon")
async def handbook(message: types.Message):

    buttons = ["Weapons",
               "Equipment sets",
               "Tool",
               "Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.reply("Choose the option that interests you",
                         reply_markup=keyboard)

# HandBook -> Other
@Dispatcher_bot.message_handler(lambda message: message.text == "Other")
async def handbook(message: types.Message):

    buttons = ["Travel",
               "Multiclassing",
               "Experience",
               "Languages",
               "Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.reply("Choose the option that interests you",
                         reply_markup=keyboard)

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

if __name__ == "__main__":
    executor.start_polling(Dispatcher_bot, skip_updates=True)