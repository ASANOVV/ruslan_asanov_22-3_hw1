from aiogram import types, Dispatcher
from config import bot, dp
from database.bot_db import sql_command_delete
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup().add(InlineKeyboardButton('NEXT', callback_data='button_call_2'))
    question = "Сколько будет 5+7?"
    answers = [
        "Одиннадцать",
        "Адиннадцать",
        "Я хз вообще"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Будет двеннадцать",
        open_period=10,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = "В каком году город Бишкек получил имя Бишкек"
    answers = [
        "1926",
        "1991",
        "1546"
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="В год независимости",
        open_period=10
    )

async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text='Удален из БД', show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith('delete '))