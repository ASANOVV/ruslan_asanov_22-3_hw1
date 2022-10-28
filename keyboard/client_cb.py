from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


cancel_button = KeyboardButton('Cancel')
start_button = KeyboardButton('start')
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(cancel_button)
start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(start_button)