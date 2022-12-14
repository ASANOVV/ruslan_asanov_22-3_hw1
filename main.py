import asyncio
from aiogram.utils import executor
from config import bot, dp
import logging
from handlers import admin, callback, client, extra, fsm_mentor, notifications, inine
from database.bot_db import sql_create


async def on_startup(_):
    asyncio.create_task(notifications.scheduler())
    sql_create()


notifications.register_handlers_notification(dp)
callback.register_handlers_callback(dp)
client.register_handlers_client(dp)
fsm_mentor.register_handlers_fsm(dp)
admin.register_handlers_admin(dp)
extra.register_handlers_extra(dp)
inine.register_handlers_inline(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
