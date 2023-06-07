import asyncio

from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils.exceptions import BadRequest

from config import CONFIG
from filters import IsAdmin
from keyboards.inline.admin.adminFormIKB import admin_cb, AdminForms
from loader import dp, bot
from states.admins.adminStates import AdminStates


@dp.message_handler(IsAdmin(), commands=["admin"])
async def admin_start(message: types.Message):
    await message.answer(text="Панель Администратора",
                         reply_markup=await AdminForms.adminMenu())
    pass


@dp.message_handler(IsAdmin(), commands=["1"])
async def registration_start(message: types.Message):
    text = "Привет! На связи Есения🥰 До вебинара 2 дня, надеюсь, ты не скучаешь!\n" \
           "У меня для тебя еще один подарок!"
    tasks = []
    for admin in CONFIG.BOT.ADMINS:
        tasks.append(bot.send_message(chat_id=admin,
                                      text=text))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(commands=["2"])
async def registration_start(message: types.Message):
    text = "Урок будет через 5 часов"
    tasks = []
    for admin in CONFIG.BOT.ADMINS:
        tasks.append(bot.send_message(chat_id=admin,
                                      text=text))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(commands=["3"])
async def registration_start(message: types.Message):
    text = "Урок будет через 15 мин"
    tasks = []
    for admin in CONFIG.BOT.ADMINS:
        tasks.append(bot.send_message(chat_id=admin,
                                      text=text))

    await asyncio.gather(*tasks, return_exceptions=True)


@dp.callback_query_handler(IsAdmin(), admin_cb.filter())
@dp.callback_query_handler(IsAdmin(), admin_cb.filter(), state=AdminStates.all_states)
async def process_admin_callback(callback: types.CallbackQuery, state: FSMContext = None):
    await AdminForms.process(callback=callback, state=state)


@dp.message_handler(IsAdmin(), state=AdminStates.all_states, content_types=["text"])
async def process_admin_message(message: types.Message, state: FSMContext):
    await AdminForms.process(message=message, state=state)
