import asyncio

from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import MediaGroup, InputFile
from aiogram.utils.exceptions import BadRequest

from config import CONFIG
from crud import CRUDUser
from filters import IsAdmin
from keyboards.inline.users.mainFormIKB import main_cb, MainForms
from loader import dp, bot
from schemas import UsersSchema
from states.users.userStates import UserStates


@dp.message_handler(commands=["start"])  # +
async def registration_start(message: types.Message):
    user = await CRUDUser.get(user_id=message.from_user.id)
    text = "Привет! Ты зарегистрировалась на мой вебинар «Как продавать свои услуги в " \
           "инстаграм и выйти на стабильный доход?»До встречи 8 октября в 13.00 📍"
    if user:
        await message.answer(text=text)
    else:
        await CRUDUser.add(user=UsersSchema(user_id=message.from_user.id))
        await message.answer(text=text)

    #827543744


@dp.message_handler(IsAdmin(), commands=["1"])  # 7 октября в 12.00
async def registration_start1(message: types.Message):
    text = "Привет! Напоминаю, что завтра мы встречаемся в 13.00 на моем вебинаре «Как эксперту продавать свои " \
           "услуги в инстаграм и выйти на стабильный доход?» Ссылку пришлю завтра за 1 час до вебинара❤️"
    tasks = []

    users = await CRUDUser.get_all()
    for user in users:
        tasks.append(bot.send_message(chat_id=user.user_id,
                                      text=text))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(IsAdmin(), commands=["2"])  # 8 октября в 12.00
async def registration_start1(message: types.Message):
    text = "Привет! Ты готова?\n" \
           "Встречаемся сегодня в 13.00!\n" \
           "Расскажу, как выйти на стабильных доход с продажи своих услуг через инстаграм!\n\n" \
           "Идентификатор конференции: 864 3709 6977\n" \
           "Код доступа: 634134\n\n" \
           "Техническая поддержка ➡️ https://t.me/sshlyomina"
    tasks = []
    link = "https://us02web.zoom.us/j/86437096977?pwd=bWxkc3R6TU1oeVA2Y1IxSVk1b2pZZz09"
    users = await CRUDUser.get_all()
    for user in users:
        tasks.append(bot.send_message(chat_id=user.user_id,
                                      text=text,
                                      reply_markup=await MainForms.gift(link=link,
                                                                        text="Ссылка"),
                                      disable_web_page_preview=True))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(IsAdmin(), commands=["3"])  # 8 октября в 12.45
async def registration_start1(message: types.Message):
    text = "Собираемся! Готовь чаек и конспект! Будет жарко 🔥\n\n" \
           "Идентификатор конференции: 864 3709 6977\n" \
           "Код доступа: 634134\n\n" \
           "Техническая поддержка ➡️ https://t.me/sshlyomina"
    tasks = []
    link = "https://us02web.zoom.us/j/86437096977?pwd=bWxkc3R6TU1oeVA2Y1IxSVk1b2pZZz09"
    users = await CRUDUser.get_all()
    for user in users:
        tasks.append(bot.send_message(chat_id=user.user_id,
                                      text=text,
                                      reply_markup=await MainForms.gift(link=link,
                                                                        text="Ссылка"),
                                      disable_web_page_preview=True
                                      ))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(IsAdmin(), commands=["4"])  # 8 октября 13.05
async def registration_start1(message: types.Message):
    text = "Ехуууу!!! Начинаем!\n" \
           "Ждем только тебя!\n\n" \
           "Идентификатор конференции: 864 3709 6977\n" \
           "Код доступа: 634134\n\n" \
           "Техническая поддержка ➡️ https://t.me/sshlyomina"

    tasks = []
    link = "https://us02web.zoom.us/j/86437096977?pwd=bWxkc3R6TU1oeVA2Y1IxSVk1b2pZZz09"
    users = await CRUDUser.get_all()
    for user in users:
        tasks.append(bot.send_message(chat_id=user.user_id,
                                      text=text,
                                      reply_markup=await MainForms.gift(link=link,
                                                                        text="Ссылка"),
                                      disable_web_page_preview=True
                                      ))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(IsAdmin(), commands=["5"])  # 8 октября 16.00
async def registration_start1(message: types.Message):
    text = "Спасибо за участие!\n" \
           "Было круто!" \
           "Ссылка на запись будет чуть позже в этом боте🥰🔥"
    tasks = []
    users = await CRUDUser.get_all()
    for user in users:
        tasks.append(bot.send_message(chat_id=user.user_id,
                                      text=text,
                                      disable_web_page_preview=True
                                      ))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(IsAdmin(), commands=["6"])  # 9 октября 10.00
async def registration_start1(message: types.Message):
    text = "Ты с нами? Это нельзя упускать!\n" \
           "Последний поток курса UP, еще и с возможностью его пройти по такой приятной цене!\n\n" \
           "Всем участникам вебинара➡️ смотри предложения\n" \
           'Есть рассрочка ➡️ ' \
           '<a href="https://onedrive.live.com/view.aspx?resid=DE1BFD4ED886970E!222&ithint=file%2Cdocx&wdo=2&authkey=!ANHrgr5JWxX9ejU">читать подробнее</a>\n\n' \
           'Чтобы забронировать место, пиши ➡️ @esenia_sergeeva \n' \
           "Если остались вопросы, не стесняйся!"
    tasks = []
    users = await CRUDUser.get_all()
    for user in users:
        tasks.append(bot.send_message(chat_id=user.user_id,
                                      text=text,
                                      disable_web_page_preview=True
                                      ))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу

    album = MediaGroup()  # /opt/git/webinarTelegramBot
    photo1 = InputFile(path_or_bytesio='/opt/git/webinarTelegramBot/p/1.jpg')
    photo2 = InputFile(path_or_bytesio='/opt/git/webinarTelegramBot/p/2.jpg')
    photo3 = InputFile(path_or_bytesio='/opt/git/webinarTelegramBot/p/3.jpg')

    tasks2 = []
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)

    users = await CRUDUser.get_all()
    for user in users:
        tasks2.append(bot.send_media_group(chat_id=user.user_id,
                                           media=album
                                           ))

    await asyncio.gather(*tasks2, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(IsAdmin(), commands=["7"])  # 13 августа в 10.00
async def registration_start1(message: types.Message):
    text = "СЕГОДНЯ ПОСЛЕДНИЙ ДЕНЬ\n" \
           "Занять свое место и научиться наконец классно продавать свои услуги, создать очередь " \
           "из клиентов и стабильно зарабатывать на любимом деле!\n" \
           "Решайся! Лучше момента уже не будет🔥\n\n" \
           "Читать подробнее о курсе ➡️ https://eseniyasergeeva.by\n" \
           "Есть рассрочка ➡️ " \
           '<a href="https://onedrive.live.com/view.aspx?resid=DE1BFD4ED886970E!222&ithint=file%2Cdocx&wdo=2&authkey=!ANHrgr5JWxX9ejU">читать подробнее</a>\n' \
           "Бронь и вопросы ➡️ @esenia_sergeeva"
    tasks = []
    users = await CRUDUser.get_all()
    for user in users:
        tasks.append(bot.send_message(chat_id=user.user_id,
                                      text=text,
                                      disable_web_page_preview=True
                                      ))
    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу

    album = MediaGroup()  # /opt/git/webinarTelegramBot
    photo1 = InputFile(path_or_bytesio='/opt/git/webinarTelegramBot/p/1.jpg')
    photo2 = InputFile(path_or_bytesio='/opt/git/webinarTelegramBot/p/2.jpg')
    photo3 = InputFile(path_or_bytesio='/opt/git/webinarTelegramBot/p/3.jpg')

    tasks2 = []
    album.attach_photo(photo=photo1)
    album.attach_photo(photo=photo2)
    album.attach_photo(photo=photo3)

    users = await CRUDUser.get_all()
    for user in users:
        tasks2.append(bot.send_media_group(chat_id=user.user_id,
                                           media=album
                                           ))

    await asyncio.gather(*tasks2, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(IsAdmin(), commands=["testAudio"])  # 13 августа в 10.00
async def registration_start1(message: types.Message):

    tasks = []
    audio = open(r'/opt/git/webinarTelegramBot/Денежная медитация.mp3', 'rb')
    tasks.append(bot.send_audio(chat_id=message.from_user.id, audio=audio))
    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу
    audio.close()


@dp.message_handler(IsAdmin(), commands=["getTXT"])  # в конце урока!!!
async def registration_start8(message: types.Message):
    text8 = "Привет, милые! ❤️\n" \
            "Я с новостью 🔥\n" \
            "В каком-то невероятном потоке и энергии благодарности и любви я написала тренинг для тех, " \
            "с кем мы точно совпадаем энергиями!\n\n" \
            "PROденьги - для тех, кто хочет построить здоровые и крепкие отношения с деньгами и " \
            "выйти из созависимости✨\n\n" \
            "31 июля в 19.00 я проведу тренинг онлайн, который нельзя будет пройти повторно и доступ к " \
            "которому будет только у тех, кто хотя бы однажды со мной контактировал! " \
            "Тренинг по любви, чтобы навсегда избавиться от мусора в голове, который мешает зарабатывать‼\n\n" \
            "🔝Цена, которая является символической, доступна только для любимых и близких➡️ 11$\n\n" \
            "Переходите по ссылке и читайте подробности"

    tasks8 = []
    link8 = "http://project7593041.tilda.ws/"
    users = await CRUDUser.get_all()
    for user in users:
        tasks8.append(bot.send_message(chat_id=user.user_id,
                                       text=text8,
                                       reply_markup=await MainForms.gift(link=link8,
                                                                         text="Ссылка")))

    await asyncio.gather(*tasks8, return_exceptions=True)


@dp.message_handler(IsAdmin(), commands=["doc"])  # в конце урока!!!
async def registration_start8(message: types.Message):
    text8 = "Есть рассрочка ➡️ читать подробнее"

    tasks8 = []
    users = await CRUDUser.get_all()
    for user in users:
        tasks8.append(bot.send_message(chat_id=user.user_id,
                                       text=text8,
                                       reply_markup=await MainForms.get_dock()))

    await asyncio.gather(*tasks8, return_exceptions=True)


@dp.message_handler(IsAdmin(), commands=["link"])  # в конце урока!!!
async def registration_startLink(message: types.Message):
    await message.answer(text='Введите ссылку:')
    await UserStates.Ping.set()


@dp.message_handler(state=UserStates.Ping)
async def process_numberPing(message: types.Message, state: FSMContext):
    try:
        CONFIG.ADDCOURSE.LINK = message.text
        await state.finish()
    except ValueError:
        await message.answer("Ошибка ввода. link")
        return


@dp.message_handler(IsAdmin(), commands=["gettxt"])  # в конце урока!!!
async def registration_startGetTXT(message: types.Message):
    await message.answer(text='Введите text')
    await UserStates.Description.set()


@dp.message_handler(state=UserStates.Description)
async def process_numberDescription(message: types.Message, state: FSMContext):
    try:
        tasks = []
        users = await CRUDUser.get_all()
        for user in users:
            tasks.append(bot.send_message(chat_id=user.user_id,
                                          text=message.text))

        await asyncio.gather(*tasks, return_exceptions=True)

        await state.finish()
    except ValueError:
        await message.answer("Ошибка ввода text")
        return


@dp.message_handler(IsAdmin(), commands=["gettxtb"])  # в конце урока!!!
async def registration_startgettxtb(message: types.Message):
    await message.answer(text='Введите text c кнопкой')
    await UserStates.DescriptionB.set()


@dp.message_handler(state=UserStates.DescriptionB)
async def process_numberDescriptionB(message: types.Message, state: FSMContext):
    try:
        CONFIG.ADDCOURSE.DESCRIPTION = message.text
        tasks = []
        users = await CRUDUser.get_all()
        for user in users:
            tasks.append(bot.send_message(chat_id=user.user_id,
                                          text=message.text,
                                          reply_markup=await MainForms.gift(link=CONFIG.ADDCOURSE.LINK,
                                                                            text="Ссылка")))

        await asyncio.gather(*tasks, return_exceptions=True)

        await state.finish()
    except ValueError:
        await message.answer("Ошибка ввода text")
        return


@dp.callback_query_handler(main_cb.filter())
@dp.callback_query_handler(main_cb.filter(), state=UserStates.all_states)
async def process_callback(callback: types.CallbackQuery, state: FSMContext = None):
    await MainForms.process(callback=callback, state=state)


@dp.message_handler(state=UserStates.all_states, content_types=["text"])
async def process_message(message: types.Message, state: FSMContext):
    await MainForms.process(message=message, state=state)
