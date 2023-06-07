import re

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import BadRequest

from config import CONFIG
from loader import bot
from states.admins.adminStates import AdminStates

admin_cb = CallbackData("admin", "target", "action", "id", "editId")


class AdminForms:
    @staticmethod
    async def back_ikb(target: str, action: str) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="◀️ Назад", callback_data=admin_cb.new(target, action, 0, 0))
                ]
            ]
        )

    @staticmethod
    async def adminMenu() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Добавить курс",
                                         callback_data=admin_cb.new('addCourse', 'getCourse', 0, 0))
                ]
            ]
        )

    @staticmethod
    async def create_add_course_buttons() -> InlineKeyboardMarkup:
        button_data = [
            ("Название", "NAME"),
            ("Описание", "DESCRIPTION"),
            ("Ключевое слово 1", "KW1"),
            ("Ключевое слово 2", "KW2"),
            ("Ключевое слово 3", "KW3"),
            ("Дата", "DT"),
            ("Ссылка", "LINK")
        ]

        keyboards = []
        for text, field in button_data:
            button_text = "✅" if getattr(CONFIG.ADDCOURSE, field, None) else "➕"
            button = InlineKeyboardButton(
                text=text,
                callback_data=admin_cb.new(0, 0, 0, 0)
            )
            status_button = InlineKeyboardButton(
                text=button_text,
                callback_data=admin_cb.new("addCourse", "get_add", field, 0)
            )
            keyboards.append([button, status_button])

        keyboards.append([InlineKeyboardButton(text="◀️ Назад", callback_data=admin_cb.new("AdminMenu", 0, 0, 0))])

        required_fields = ['NAME', 'DESCRIPTION', 'KW1', 'KW2', 'KW3', 'DT', 'LINK']
        if all(getattr(CONFIG.ADDCOURSE, field, None) for field in required_fields):
            keyboards.append([InlineKeyboardButton(text="Продолжить ➡️", callback_data=admin_cb.new("addCourse",
                                                                                                    "continueAdd",
                                                                                                    0, 0)
                                                   )
                              ]
                             )

        keyboard = InlineKeyboardMarkup(inline_keyboard=keyboards)
        return keyboard

    @staticmethod
    async def continueAddIKB() -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="Завершить ✅", callback_data=admin_cb.new("addCourse",
                                                                                        "", 0, 0)),
                    InlineKeyboardButton(text="Отменить ❌", callback_data=admin_cb.new("addCourse",
                                                                                       "", 0, 0))
                ],
                [
                    InlineKeyboardButton(text="◀️ Назад", callback_data=admin_cb.new("addCourse", "getCourse", 0, 0))
                ]
            ]
        )

    @staticmethod
    async def process(callback: CallbackQuery = None, message: Message = None, state: FSMContext = None) -> None:
        if callback:
            if callback.data.startswith("admin"):
                data = admin_cb.parse(callback_data=callback.data)

                if data.get("target") == "AdminMenu":
                    await state.finish()
                    await callback.message.edit_text(text="Админ Панель",
                                                     reply_markup=await AdminForms.adminMenu())

                elif data.get("target") == "addCourse":
                    if data.get('action') == "getCourse":
                        await callback.message.edit_text(text="Заполните данные",
                                                         reply_markup=await AdminForms.create_add_course_buttons())
                    elif data.get('action') == 'get_add':
                        nameField = {
                            "NAME": "Введите название курса",
                            "DESCRIPTION": " Введите описание курса",
                            "KW1": "Введите ключевое слово 1",
                            "KW2": "Введите ключевое слово 2",
                            "KW3": "Введите ключевое слово 3",
                            "DT": "Введите дату",
                            "LINK": "Вставьте ссылку на курс",
                        }

                        get_id_addCourse_IKB = data.get('id')
                        if get_id_addCourse_IKB in nameField:
                            await callback.message.edit_text(text=nameField[get_id_addCourse_IKB],
                                                             reply_markup=await AdminForms.back_ikb(target="addCourse",
                                                                                                    action="getCourse")
                                                             )

                        await state.update_data(nameField=get_id_addCourse_IKB.upper())
                        await AdminStates.addData.set()
                    elif data.get('action') == 'continueAdd':
                        text = f"Название курса - <i>{CONFIG.ADDCOURSE.NAME}</i>\n\n" \
                               f"Описание курса - <i>{CONFIG.ADDCOURSE.DESCRIPTION}</i>\n\n" \
                               f"Дата - <i>{CONFIG.ADDCOURSE.DT}\n\n</i>" \
                               f"Ссылка на курс - <i>{CONFIG.ADDCOURSE.LINK}</i>"

                        await callback.message.edit_text(text=f"Потвердите ввод\n\n{text}",
                                                         reply_markup=await AdminForms.continueAddIKB(),
                                                         parse_mode="HTML",
                                                         disable_web_page_preview=True)

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
                if await state.get_state() == "AdminStates:addData":
                    data_state = await state.get_data()
                    dataValid = False
                    match data_state['nameField']:
                        case "NAME":
                            nameField = "Название"
                            CONFIG.ADDCOURSE.NAME = message.text
                            dataValid = True
                        case "DESCRIPTION":
                            nameField = "Описание курса"
                            CONFIG.ADDCOURSE.DESCRIPTION = message.text
                            dataValid = True
                        case "KW1":
                            nameField = "Первое ключевое слово"
                            CONFIG.ADDCOURSE.KW1 = message.text
                            dataValid = True
                        case "KW2":
                            nameField = "Второе ключевое слово"
                            CONFIG.ADDCOURSE.KW2 = message.text
                            dataValid = True
                        case "KW3":
                            nameField = "Третье Ключевое слово"
                            CONFIG.ADDCOURSE.KW3 = message.text
                            dataValid = True
                        case "DT":
                            from datetime import datetime
                            nameField = "Дату"
                            date_input = message.text
                            input_date = datetime.strptime(date_input, "%d.%m.%Y")
                            current_date = datetime.now()

                            if input_date >= current_date:
                                pattern = r"^\d{2}\.\d{2}\.\d{4}$"
                                if re.match(pattern, message.text):
                                    CONFIG.ADDCOURSE.DT = message.text
                                    dataValid = True
                                else:
                                    await AdminStates.addData.set()
                                    await state.update_data(nameField="DT")
                                    await message.answer(text="Дата введена не верно!\n"
                                                              "попробуйте еще раз (00.00.0000)")
                            else:
                                await AdminStates.addData.set()
                                await state.update_data(nameField="DT")
                                await message.answer(text='Я не умею работать в прошлом!\n'
                                                          'Попробуйте еще раз ввести дату')

                            #pattern = r"^\d{2}\.\d{2}\.\d{4}$"
                            # if re.match(pattern, message.text):
                            #     print("Верный формат даты")
                            #     CONFIG.ADDCOURSE.DT = message.text
                            #     dataValid = True
                            # else:
                            #     await AdminStates.addData.set()
                            #     await state.update_data(nameField="DT")
                            #     await message.answer(text="Дата введена не верно!\n"
                            #                               "попробуйте еще раз (00.00.0000)")
                        case "LINK":
                            nameField = "Ссылку"
                            CONFIG.ADDCOURSE.LINK = message.text
                            dataValid = True
                        case _:
                            print("The language doesn't matter, what matters is solving problems.")

                    if dataValid:
                        await message.answer(text=f'Вы успешно добавили {nameField}',
                                             reply_markup=await AdminForms.create_add_course_buttons())
