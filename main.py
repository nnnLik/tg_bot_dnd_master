from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram import (Bot, Dispatcher,
                     executor, types)

from random import (randint, choice,
                    )

from os import getenv
from sys import exit

import collections
import logging
import string
import os

import config
import info_text

# Bot object
Bot = Bot(token=config.Token, parse_mode=types.ParseMode.HTML)

# var
Greating = '''
Hi
'''
storage = MemoryStorage()

Dispatcher_bot = Dispatcher(Bot, storage=storage)
logging.basicConfig(level=logging.INFO)

class FSMInputName(StatesGroup):
    name = State()

# logs
@Dispatcher_bot.message_handler(lambda message: message.text)
async def logs(message: types.Message):
    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)


# Main menu
@Dispatcher_bot.message_handler(commands="start")
async def main_menu(message: types.Message):

    buttons = ["Handbook",
               "Create Hero",
               "Generate Loot",
               "Generate Mobs",
               "Music",
               "Dice"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer(Greating, reply_markup=keyboard)


# HandBook
@Dispatcher_bot.message_handler(lambda message: message.text == "Handbook")
async def handbook(message: types.Message):

    buttons = ["Movement/Action",
               "Rest",
               "Damage",
               "Weapon",
               "Other",
               "Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer("Here you can find all the <b>basic information</b>, which has been divided into parts for your convenience.",
                         reply_markup=keyboard)

    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)

# Create Hero
@Dispatcher_bot.message_handler(lambda message: message.text == "Create Hero")
async def send_file(message: types.Document):

    name_of_hero_list = choice(os.listdir(config.dir_hero_lists))
    await message.reply_document(open(config.dir_hero_lists + name_of_hero_list, 'rb'))
    get_name_list = name_of_hero_list[:-4].replace('-', ' ').replace('lss', '').replace('male', '').capitalize()
    await message.answer(f'Your warrior today will be <b>{get_name_list}</b>')

    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)

# HandBook -> Movement/Action
@Dispatcher_bot.message_handler(lambda message: message.text == "Movement/Action")
async def handbook_mov_act(message: types.Message):

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

    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)


# HandBook -> Movement/Action -> Movement
@Dispatcher_bot.message_handler(lambda message: message.text == "Movement")
async def handbook_movement(message: types.Message):
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

    await message.answer(info_text.movement, reply_markup=get_inline_keyboard_for_movement())
    await message.answer('❓', reply_markup=keyboard)

    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)


# HandBook -> Movement/Action -> Action
@Dispatcher_bot.message_handler(lambda message: message.text == "Action")
async def handbook_action(message: types.Message):
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

    await message.answer(info_text.action, reply_markup=get_inline_keyboard_for_movement())
    await message.answer('❓', reply_markup=keyboard)

    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)

# HandBook -> State
@Dispatcher_bot.message_handler(lambda message: message.text == "Rest")
async def handbook_state(message: types.Message):

    buttons = ["State",
               "Environment and Perception",
               "Hits, Death, and Rest",
               "Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer("Choose the option that interests you",
                         reply_markup=keyboard)

    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)

# HandBook -> Damage
@Dispatcher_bot.message_handler(lambda message: message.text == "Damage")
async def handbook_damage(message: types.Message):

    buttons = ["Damage and Attacks",
               "Spells",
               "Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer("Choose the option that interests you",
                         reply_markup=keyboard)

    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)

# HandBook -> Weapon
@Dispatcher_bot.message_handler(lambda message: message.text == "Weapon")
async def handbook_weapon(message: types.Message):

    buttons = ["Weapons",
               "Equipment sets",
               "Tool",
               "Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer("Choose the option that interests you",
                         reply_markup=keyboard)

    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)

# HandBook -> Other
@Dispatcher_bot.message_handler(lambda message: message.text == "Other")
async def handbook_other(message: types.Message):

    buttons = ["Travel",
               "Multiclassing",
               "Experience",
               "Languages",
               "Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer("Choose the option that interests you",
                         reply_markup=keyboard)

    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)

async def throw_dice(faces=4):
    await message.answer('1', reply_markup=keyboard)
    for i in string.digits:
        await message.edit_text(i)

@Dispatcher_bot.message_handler(lambda message: message.text == "Dice")
async def handbook_other(message: types.Message):

    buttons = ["Back to Menu"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer('Enter a number that will reflect the number of faces of the <b><u>cube</u></b>', reply_markup=keyboard)
    await message.answer('The number of faces can be from 2 to 100', reply_markup=keyboard)

    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)

    await FSMInputName.name.set()


@Dispatcher_bot.message_handler(state=FSMInputName.name)
async def state1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    def throw(faces):
        fin_dice_value = randint(0, faces)
        return  fin_dice_value

    config.wr_faces(message.text)
    faces_of_dice = config.rd_faces()

    await message.answer(throw(faces_of_dice))

    await state.finish()


# Return to main menu
@Dispatcher_bot.message_handler(lambda message: message.text == "Back to Menu")
async def back_menu(message: types.Message):

    buttons = ["Handbook",
               "Create Hero",
               "Generate Loot",
               "Generate Mobs",
               "Music",
               "Dice"]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    await message.answer('<b>Whoo</b>', reply_markup=keyboard)

    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)

# Features that are currently under development
@Dispatcher_bot.callback_query_handler(text="alpha_test")
async def add_inf(call: types.CallbackQuery):
    await call.message.answer('This feature is being developed. Everything will be ready soon')

    config.log(id=message.from_user.id, name=message.from_user.full_name, text=message.text)

# ---------------------

if __name__ == "__main__":
    # Start bot
    executor.start_polling(Dispatcher_bot, skip_updates=True)