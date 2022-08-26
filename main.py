from aiogram import (Bot, Dispatcher,
                     executor, types)
from random import (randint, choice,
                    )

from os import getenv
from sys import exit

import logging
import config
import os

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

    await message.answer("Choose the option that interests you",
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

    await message.answer("Choose the option that interests you",
                         reply_markup=keyboard)

# HandBook -> Damage
@Dispatcher_bot.message_handler(lambda message: message.text == "Damage")
async def handbook(message: types.Message):

    buttons = ["Damage and Attacks",
               "Spells",
               "Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer("Choose the option that interests you",
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

    await message.answer("Choose the option that interests you",
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

    await message.answer("Choose the option that interests you",
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


# HandBook -> Movement/Action -> Movement
@Dispatcher_bot.message_handler(lambda message: message.text == "Movement")
async def handbook(message: types.Message):
    def get_inline_keyboard_for_movement():
        # Generate Keyboard
        inline_buttons = [
            types.InlineKeyboardButton(text="1", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="2", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="3", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="4", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="5", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="6", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="7", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="8", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="9", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="10", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="11", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="12", callback_data="alpha_test"),
        ]

        inline_keyboard = types.InlineKeyboardMarkup(row_width=3)
        inline_keyboard.add(*inline_buttons)
        return inline_keyboard

    buttons = ["Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer('''
    You can move at any time during your turn (before, after, or during actions).\n\n
    1) <b>Move</b>
    Cost: 5 feet per move 5 feet

    2) <b>Climbing</b>
    Cost: 10 feet for climbing 5 feet

    3) <b>Swimming</b>
    Cost: 10 feet for 5 feet swim

    4) <b>Fall prone</b>
    Cost: 0 feet

    5) <b>Crawling</b>
    Cost: 10 feet per 5 feet crawl

    6) <b>Getting up</b>
    Cost: Half movement speed

    7) <b>High jump</b>
    Cost: 5 feet per 5 feet of jump

    8) <b>Long jump</b>
    Cost: 5 feet per 5 feet of jump

    9) <b>Improvisation</b>
    Perform any move or trick

    10) <b>Difficult terrain</b>
    Moving on difficult terrain. Cost: +5 feet per 5 feet

    11) <b>Movement in capture</b>
    Pushing or carrying a grabbed creature. Cost: Speed is halved

    12) <b>Mounting and dismounting</b>
    Sit or dismount from a mount. Cost: Half movement speed


    ''', reply_markup=get_inline_keyboard_for_movement())
    await message.answer('❓', reply_markup=keyboard)

# HandBook -> Movement/Action -> Action
@Dispatcher_bot.message_handler(lambda message: message.text == "Action")
async def handbook(message: types.Message):
    def get_inline_keyboard_for_movement():
        # Generate Keyboard
        inline_buttons = [
            types.InlineKeyboardButton(text="1", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="2", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="3", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="4", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="5", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="6", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="7", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="8", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="9", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="10", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="11", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="12", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="13", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="14", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="15", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="16", callback_data="alpha_test"),
            types.InlineKeyboardButton(text="17", callback_data="alpha_test"),
        ]

        inline_keyboard = types.InlineKeyboardMarkup(row_width=3)
        inline_keyboard.add(*inline_buttons)
        return inline_keyboard

    buttons = ["Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer('''
    1) <b>Attack</b>
    Make one melee or ranged attack
    
    2) <b>Push</b>
    Push a creature to knock it down or push it further away from you
    
    3) <b>Snatch</b>
    Until the end of the current turn, your speed is doubled
    
    4) <b>Evasion</b>
    Focus on dodging attacks
    
    5) <b>Help</b>
    Provide assistance to another creature by granting advantage on a check
    
    6) <b>Take a shield</b>
    Put on or take off a shield
    
    7) <b>Search</b>
    Give full attention to finding something
    
    8) <b>Preparation</b>
    Selecting a condition and its corresponding action
    
    9) <b>Improvisation</b>
    Any other action you may
    submit and execute
    
    10) <b>Capture</b>
    Attempt to grab a creature or wrestle
    
    11) <b>Casting a spell</b>
    Cast a spell with a 1-action casting time
    
    12) <b>Waste</b>
    Move without provoking an attack
    
    13) <b>Release</b>
    Attempt to release from the grip or from the shackles
    
    14) <b>Using the item</b>
    Interacting with a second item or using special properties
    
    15) <b>Ambush</b>
    Trying to get out of sight
    
    16) <b>Stabilization</b>
    Stabilize the state of an unconscious being
    
    17) <b>Class Ability</b>
    Using an ability of your class or race that requires an action


    ''', reply_markup=get_inline_keyboard_for_movement())
    await message.answer('❓', reply_markup=keyboard)

@Dispatcher_bot.callback_query_handler(text="alpha_test")
async def add_inf(call: types.CallbackQuery):
    await message.answer('This feature is being developed. Everything will be ready soon')

@Dispatcher_bot.message_handler(commands='file')
async def send_file(message: types.Document):
    await message.reply_document(open('hero_lists/dwarf-druid-male-lss.pdf', 'rb'))


# ----------------

if __name__ == "__main__":
    executor.start_polling(Dispatcher_bot, skip_updates=True)