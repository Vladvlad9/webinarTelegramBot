from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BadRequest

from loader import bot

main_cb = CallbackData("main", "target", "id", "editId")


class MainForms:
    @staticmethod
    async def back_ikb(target: str) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="◀️ Назад", callback_data=main_cb.new(target, 0, 0))
                ]
            ]
        )

    @staticmethod
    async def gift(link: str, text: str) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=text,
                                         url=link,
                                         callback_data=main_cb.new(0, 0, 0))
                ]
            ]
        )

    @staticmethod
    async def mainMenu() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Кнопка", callback_data=main_cb.new(0, 0, 0))
                ]
            ]
        )

    @staticmethod
    async def process(callback: CallbackQuery = None, message: Message = None, state: FSMContext = None) -> None:
        if callback:
            if callback.data.startswith("main"):
                data = main_cb.parse(callback_data=callback.data)

                if data.get("target") == "MainMenu":
                    text = "Привет! Ты зарегистрирована на вебинар «Клиенты из инстаграм», " \
                           "который пройдет 20 июня в 19.00.\n" \
                           "Персональная ссылка придет прямо в этот бот.\n" \
                           "Мы обязательно оповестим заранее и ты точно не пропустишь! До встречи 20 июня❤\n️" \
                           "А сейчас нажми #start чтобы посмотреть вебинар «Как приручить страх»"

                    await callback.message.edit_text(text=text,
                                                     reply_markup=await MainForms.mainMenu())

        if message:
            await message.delete()

            try:
                await bot.delete_message(
                    chat_id=message.from_user.id,
                    message_id=message.message_id - 1
                )
            except BadRequest:
                pass

            if state:
                pass