from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random
from database.bot_db import sql_command_random

async def start_command(message: types.Message):
    await message.answer(f'Здарова как поживаеш {message.from_user.full_name}')


async def dice_game(message: types.Message):
    games = ['⚽', '️🏀', '🎲', '🎰', '🎳', '🎯']
    g = random.choice(games)
    await bot.send_dice(message.chat.id, emoji=g)


async def mem_command(message: types.Message):
    mem_photo = open("media/mem1.jpg", "rb")
    await bot.send_photo(message.chat.id, mem_photo)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("След.", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Кто придумал C++"
    answers = [
        'Бог',
        'Никлаус Вирт',
        'Нашальникаа',
        'Бьёрн Страуструп',
        'Никлаус Вирт',
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="ЕГО ПРИДУМАЛ САТАНА",
        open_period=30,
        reply_markup=markup
    )


async def get_random_mentor(message: types.Message):
    await sql_command_random(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(mem_command, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(dice_game, commands=["game"])
    dp.register_message_handler(get_random_mentor, commands=['get'])
