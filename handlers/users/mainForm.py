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


@dp.message_handler(commands=["newtest"])  # +
async def registration_start(message: types.Message):
    with open('1.txt') as f:
        for i in f:
            await CRUDUser.addNew(user=UsersSchema(user_id=int(i)))


@dp.message_handler(commands=["start"])  # +
async def registration_start(message: types.Message):
    user = await CRUDUser.get(user_id=message.from_user.id)
    text = " Привет! Ты зарегистрирована на тренинг PROденьги 🎉 \n" \
           "Встретимся 31 июля в 19.00! \n" \
           "Ссылку дам в день тренинга! Спасибо за доверие❤️"

    if user:
        await message.answer(text=text)
    else:
        await CRUDUser.add(user=UsersSchema(user_id=message.from_user.id))
        await message.answer(text=text)

    #827543744


@dp.message_handler(IsAdmin(), commands=["1"])  # 30 июля в 10.00
async def registration_start1(message: types.Message):
    text = "Привет! Надеюсь, ты не забыла, что завтра мы встретимся онлайн на моем тренинге PROденьги!\n" \
           "31 июля в 19.00!\n" \
           "Приготовь блокнот и ручку: будет много инсайтов и упражнения💫"
    tasks = []

    users = await CRUDUser.get_all()
    for user in users:
        tasks.append(bot.send_message(chat_id=user.user_id,
                                      text=text))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(IsAdmin(), commands=["2"])  # 31 июля в 14.00
async def registration_start1(message: types.Message):
    text = "Привет! Встречаемся сегодня в 19.00!\n" \
           "Техническая поддержка ➡️ https://t.me/sshlyomina"
    tasks = []
    link = "https://us02web.zoom.us/j/85184416076?pwd=djZYeHlCNUR4UWhLd1hGQkp6Y29wZz09"
    users = await CRUDUser.get_all()
    for user in users:
        tasks.append(bot.send_message(chat_id=user.user_id,
                                      text=text,
                                      reply_markup=await MainForms.gift(link=link,
                                                                        text="Ссылка"),
                                      disable_web_page_preview=True))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(IsAdmin(), commands=["3"])  # 31 июля в 18.45
async def registration_start1(message: types.Message):
    text = "Через 15 минут начинаем! Жду тебя по ссылке\n" \
           "Техническая поддержка ➡️ https://t.me/sshlyomina"
    tasks = []
    link = "https://us02web.zoom.us/j/85184416076?pwd=djZYeHlCNUR4UWhLd1hGQkp6Y29wZz09"
    users = await CRUDUser.get_all()
    for user in users:
        tasks.append(bot.send_message(chat_id=user.user_id,
                                      text=text,
                                      reply_markup=await MainForms.gift(link=link,
                                                                        text="Ссылка"),
                                      disable_web_page_preview=True
                                      ))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(IsAdmin(), commands=["4"])  # 31 июля в 22.00
async def registration_start1(message: types.Message):
    text = "Мы закончили! Запись я размещу в боте (здесь) завтра! " \
           "Она будет доступна 1 месяц и ты сможешь посмотреть тренинг в любое удобное для тебя время❤️"
    tasks = []
    link = "https://us02web.zoom.us/j/85184416076?pwd=djZYeHlCNUR4UWhLd1hGQkp6Y29wZz09"
    users = await CRUDUser.get_all()
    for user in users:
        tasks.append(bot.send_message(chat_id=user.user_id,
                                      text=text,
                                      reply_markup=await MainForms.gift(link=link,
                                                                        text="Ссылка"),
                                      disable_web_page_preview=True
                                      ))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу


@dp.message_handler(IsAdmin(), commands=["5"])  # 1 августа в 10.00
async def registration_start1(message: types.Message):
    text = "Привет! Запись вебинара доступна по ссылке ➡️ В доступе она останется на месяц✨"
    tasks = []
    link = "https://us02web.zoom.us/j/85184416076?pwd=djZYeHlCNUR4UWhLd1hGQkp6Y29wZz09"
    users = await CRUDUser.get_all()
    for user in users:
        tasks.append(bot.send_message(chat_id=user.user_id,
                                      text=text,
                                      reply_markup=await MainForms.gift(link=link,
                                                                        text="Ссылка"),
                                      disable_web_page_preview=True
                                      ))

    await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу

# @dp.message_handler(commands=["start"])  # +
# async def registration_start(message: types.Message):
#     user = await CRUDUser.get(user_id=message.from_user.id)
#     text = "Привет! Ты зарегистрирована на вебинар «Клиенты из инстаграм», " \
#            "который пройдет 29 июня в 19.00.\n\n" \
#            "Персональная ссылка придет прямо в этот бот.\n\n" \
#            "Мы обязательно оповестим заранее и ты точно не пропустишь! До встречи 29 июня❤\n️" \
#            "А сейчас можешь посмотреть вебинар «Как приручить страх»\n\n"
#     link = "https://youtu.be/NN_itUaYxBI"
#     if user:
#         await message.answer(text=text, reply_markup=await MainForms.gift(link=link,
#                                                                           text="Посмотреть вебинар"))
#     else:
#         await CRUDUser.add(user=UsersSchema(user_id=message.from_user.id))
#         await message.answer(text=text, reply_markup=await MainForms.gift(link=link,
#                                                                           text="Посмотреть вебинар"))
#
#     #827543744


# @dp.message_handler(IsAdmin(), commands=["1"])  # сдлеать за 2 дня +
# async def registration_start1(message: types.Message):
#     text = "Привет! На связи Есения🥰 До вебинара 2 дня, надеюсь, ты не скучаешь!\n" \
#            "У меня для тебя еще один подарок!"
#     tasks = []
#     link = "https://www.youtube.com/watch?v=dq-Ixul691U&feature=youtu.be&ab_channel=%D0%95%D1%81%D0%B5%D0%BD%D0%B8%D1%8F%D0%A1%D0%B5%D1%80%D0%B3%D0%B5%D0%B5%D0%B2%D0%B0"
#     users = await CRUDUser.get_all()
#     for user in users:
#         tasks.append(bot.send_message(chat_id=user.user_id,
#                                       text=text,
#                                       reply_markup=await MainForms.gift(link=link, text='Скорее жми «подарок»')))
#
#     await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу
#
#
# @dp.message_handler(IsAdmin(), commands=["2"])  # сделать в этот день в 10:00 +
# async def registration_start2(message: types.Message):
#     text = "Привет! Этот день настал! Встречаемся сегодня в 19.00 по мск❤️\n" \
#            "Что будет на вебинаре?\n" \
#            "💡Почему стоит выводить бизнес в инстаграм?\n" \
#            "💡Откуда там берутся клиенты?\n" \
#            "💡Как упаковать профиль, чтобы покупали?\n" \
#            "💡Как выделиться среди конкурентов?\n" \
#            "💡Как сделать монетизировать контент?\n" \
#            "💡Как регулярно зарабатывать на любимом деле?\n\n" \
#            "Присоединяйся! Дам пошаговую схему построения продаж в любой нише в инстаграм🔥\n" \
#            "Ссылка на трансляцию придет за час до вебинара"
#
#     tasks = []
#     users = await CRUDUser.get_all()
#     for user in users:
#         tasks.append(bot.send_message(chat_id=user.user_id,
#                                       text=text))
#
#     await asyncio.gather(*tasks, return_exceptions=True)  # Отправка всем админам сразу
#
#
# @dp.message_handler(IsAdmin(), commands=["3"])  # за час до начала +
# async def registration_start3(message: types.Message):
#     text = "Это снова я, Есения Сергеева. Уже через час встречаемся с вами на моем вебинаре «Клиенты из инстаграм»\n"
#     tasks = []
#     link = "https://us02web.zoom.us/j/82556383687?pwd=V1VmMkgyQlpEQUxxUXpKRU0xYWpRUT09"
#     users = await CRUDUser.get_all()
#     for user in users:
#         tasks.append(bot.send_message(chat_id=user.user_id,
#                                       text=text,
#                                       reply_markup=await MainForms.gift(link=link,
#                                                                         text="‼️Вот ваша ссылка на вебинарную комнату ➡")))
#
#     await asyncio.gather(*tasks, return_exceptions=True)
#
#
# @dp.message_handler(IsAdmin(), commands=["4"])  # за 15 минут #Добавить ссылку через Config
# async def registration_start4(message: types.Message):
#     text = "Привет, на связи Есения!\n" \
#            "Через 15 минут встретимся в прямом эфире🔥\n\n" \
#            "Готовь ручку и блокнот! Будет, как обычно, четко и по делу😉\n\n" \
#            "Идентификатор конференции: 825 5638 3687\n" \
#            "Код доступа: 860148\n\n" \
#            "Техническая поддержка ➡️ https://t.me/sshlyomina\n"
#     tasks = []
#     link = "https://us02web.zoom.us/j/82556383687?pwd=V1VmMkgyQlpEQUxxUXpKRU0xYWpRUT09"
#     users = await CRUDUser.get_all()
#     for user in users:
#         tasks.append(bot.send_message(chat_id=user.user_id,
#                                       text=text,
#                                       reply_markup=await MainForms.gift(link=link,
#                                                                         text="Ссылка на вход"),
#                                       disable_web_page_preview=True))
#
#     await asyncio.gather(*tasks, return_exceptions=True)
#
#
# @dp.message_handler(IsAdmin(), commands=["5"])  # когда начнется начнется урок в 19:00 #Добавить ссылку через Config
# async def registration_start5(message: types.Message):
#     text = "Мы уже начали- ждем тебя! Прямо сейчас рассказываю, " \
#            "какие ошибки допускают мастера и эксперты и недополучают клиентов и деньги! \n"
#
#     tasks = []
#     link = "https://us02web.zoom.us/j/82556383687?pwd=V1VmMkgyQlpEQUxxUXpKRU0xYWpRUT09"
#     users = await CRUDUser.get_all()
#     for user in users:
#         tasks.append(bot.send_message(chat_id=user.user_id,
#                                       text=text,
#                                       reply_markup=await MainForms.gift(link=link,
#                                                                         text="Переходи ➡")))
#
#     await asyncio.gather(*tasks, return_exceptions=True)
#
#
# @dp.message_handler(IsAdmin(), commands=["6"])  # во время урока нужно уточнить время!!! #Добавить ссылку через Config
# async def registration_start6(message: types.Message):
#     text = "Ты еще не с нами? Прямо сейчас я разбираю поэтапную схему как сделать 1000$ в месяц на бровках, " \
#            "а позже перейду к разбору продажи курсов.\n" \
#            "Присоединяйся!\n"
#
#     tasks = []
#     link = "https://us02web.zoom.us/j/82556383687?pwd=V1VmMkgyQlpEQUxxUXpKRU0xYWpRUT09"
#     users = await CRUDUser.get_all()
#     for user in users:
#         tasks.append(bot.send_message(chat_id=user.user_id,
#                                       text=text, reply_markup=await MainForms.gift(link=link,
#                                                                                    text="Вот ссылка в вебинарную комнату")))
#
#     await asyncio.gather(*tasks, return_exceptions=True)
#
#
# @dp.message_handler(IsAdmin(), commands=["7"])  # в конце урока!!!
# async def registration_start7(message: types.Message):
#     text = "Привет! Это снова я, Есения Сергеева. Только что я рассказала о том, " \
#            "как получать клиентов из инстаграм в теории.\n" \
#            "Но бизнес- это регулярная практика и система!\n" \
#            "Именно построением такой системы мы будем заниматься на моем курсе UP.\n" \
#            "Курс стартует 7 июля. Оплатить его можно в рассрочку🔥\n" \
#            "Для этого забронируйте место на курсе по специальной цене в течение суток⬇️"
#
#     text8 = "Или напишите мне, чтобы обсудить участие и варианты оплаты"
#
#     tasks = []
#     tasks8 = []
#
#     link = "https://eseniyasergeeva.by"
#     link8 = "https://t.me/esenia_sergeeva"
#
#     users = await CRUDUser.get_all()
#     for user in users:
#         tasks.append(bot.send_message(chat_id=user.user_id,
#                                       text=text,
#                                       reply_markup=await MainForms.gift(link=link,
#                                                                         text="Забронировать место")))
#
#         tasks8.append(bot.send_message(chat_id=user.user_id,
#                                        text=text8,
#                                        reply_markup=await MainForms.gift(link=link8,
#                                                                          text="Ссылка на мой тг")))
#
#     await asyncio.gather(*tasks, return_exceptions=True)
#     await asyncio.gather(*tasks8, return_exceptions=True)
#
#
# @dp.message_handler(IsAdmin(), commands=["8"])  # в конце урока!!!
# async def registration_start8(message: types.Message):
#     text8 = "Или напишите мне, чтобы обсудить участие и варианты оплаты"
#
#     tasks8 = []
#     link8 = "https://t.me/esenia_sergeeva"
#     users = await CRUDUser.get_all()
#     for user in users:
#         tasks8.append(bot.send_message(chat_id=user.user_id,
#                                        text=text8,
#                                        reply_markup=await MainForms.gift(link=link8,
#                                                                          text="Ссылка на мой тг")))
#
#     await asyncio.gather(*tasks8, return_exceptions=True)
#
#
# @dp.message_handler(IsAdmin(), commands=["9"])  # в конце урока!!!
# async def registration_start10(message: types.Message):
#     users = await CRUDUser.get_all()
#     tasks = []
#     tasks2 = []
#     tasks3 = []
#     tasks4 = []
#     tasks5 = []
#
#     tasks2Text = 'Привет! Это снова я, Есения Сергеева. Только что я рассказала о том, ' \
#                  'как получать клиентов из инстаграм в теории.\n' \
#                  'Но бизнес- это регулярная практика и система!\n ' \
#                  'Именно построением такой системы мы будем заниматься на моем курсе UP.\n' \
#                  'Курс стартует 7 июля. Оплатить его можно в рассрочку🔥'
#
#     tasks3Text = "Чтобы забронировать место на курсе по специальной цене в " \
#                  "течение суток и оплатить полностью, выберите тариф из предложенных ниже⬇️"
#
#     tasks4Text = "Чтобы забронировать место и внести предоплату 100 byn на любой тариф, перейдите на " \
#                  "сайт и в окошке «выбрать тариф» нажмите необходимый⬇️"
#
#     tasks5Text = "Чтобы получить подробности о рассрочке, нажми сюда⬇️️"
#
#     album = MediaGroup()
#     photo1 = InputFile(path_or_bytesio='/opt/git/webinarTelegramBot/1.jpg')
#     photo2 = InputFile(path_or_bytesio='/opt/git/webinarTelegramBot/2.jpg')
#
#     album.attach_photo(photo=photo1)
#     album.attach_photo(photo=photo2)
#
#     link3 = "https://1drv.ms/w/s!Ag6XhthO_RvegV7R64K-SVsV_Xo1"
#
#     for user in users:
#         tasks.append(bot.send_media_group(chat_id=user.user_id, media=album))
#         tasks2.append(bot.send_message(chat_id=user.user_id, text=tasks2Text,
#                                        reply_markup=await MainForms.gift(link="https://eseniyasergeeva.by",
#                                                                          text="Сайт")))
#
#         tasks3.append(bot.send_message(chat_id=user.user_id, text=tasks3Text,
#                                        reply_markup=await MainForms.gift2(link="https://checkout.bepaid.by/v2/confirm_order/prd_f83d0244e5287e22/21195",
#                                                                           text="я сама 444 byn",
#                                                                           link2="https://checkout.bepaid.by/v2/confirm_order/prd_985dcc14f7acd5c1/21195",
#                                                                           text2="vip 1300 byn")))
#
#         tasks4.append(bot.send_message(chat_id=user.user_id, text=tasks4Text,
#                                        reply_markup=await MainForms.gift(link="https://eseniyasergeeva.by",
#                                                                          text="Сайт")))
#
#         tasks5.append(bot.send_message(chat_id=user.user_id,
#                                        text=tasks5Text,
#                                        reply_markup=await MainForms.gift(link=link3, text="Рассрочка")))
#
#     await asyncio.gather(*tasks, return_exceptions=True)
#     await asyncio.gather(*tasks2, return_exceptions=True)
#     await asyncio.gather(*tasks3, return_exceptions=True)
#     await asyncio.gather(*tasks4, return_exceptions=True)
#     await asyncio.gather(*tasks5, return_exceptions=True)
#
#
# @dp.message_handler(IsAdmin(), commands=["10"])  # в конце урока!!!
# async def registration_start9(message: types.Message):
#     text = "Осталось 12 часов до повышения цены!\n" \
#            "Привет! Через 12 часов цена на обучение вырастет и ты еще успеваешь запрыгнуть в последний вагон!\n" \
#            "Успевай забронировать место по приятной цене и приходи выстраивать бизнес из своего " \
#            "любимого дела на курс «UP»\n" \
#            "Курс стартует 7 июля.\n" \
#            "Оплатить его можно в рассрочку."
#
#     text8 = "Или напишите мне, чтобы обсудить участие и варианты оплаты"
#
#     tasks = []
#     tasks8 = []
#
#     link = "https://eseniyasergeeva.by"
#     link8 = "https://t.me/esenia_sergeeva"
#
#     users = await CRUDUser.get_all()
#     for user in users:
#         tasks.append(bot.send_message(chat_id=user.user_id,
#                                       text=text,
#                                       reply_markup=await MainForms.gift(link=link, text="Забронировать место")))
#
#         tasks8.append(bot.send_message(chat_id=user.user_id,
#                                        text=text8,
#                                        reply_markup=await MainForms.gift(link=link8,
#                                                                          text="Ссылка на мой тг")))
#
#     await asyncio.gather(*tasks, return_exceptions=True)
#     await asyncio.gather(*tasks8, return_exceptions=True)
#
#
# @dp.message_handler(IsAdmin(), commands=["11"])  # в конце урока!!!
# async def registration_start10(message: types.Message):
#     text = "Осталось всего 3 часа..\n" \
#            "Сколько можно откладывать свои желания? Жизнь - это то, что происходит здесь и сейчас!\n" \
#            "Через 3 часа спецпредложение закончится, поэтому успевай забрать свой последний шанс и " \
#            "забронировать место на курс!\n" \
#            "Наличие мест:\n" \
#            "✨VIP с Есенией 2\n\n" \
#            "Бронируй свое место, оплачивай в рассрочку и начнем строить дело мечты, приносящее деньги, " \
#            "а не проблемы ❤️\n" \
#            "Стартуем 7 июля! Запрыгивай "
#
#     txt2 = "Или напишите мне, чтобы обсудить участие и варианты оплаты"
#     tasks3Text = "Чтобы получить подробности о рассрочке, нажми сюда⬇️️"
#
#     tasks = []
#     tasks2 = []
#     tasks3 = []
#
#     link = "https://eseniyasergeeva.by"
#     link2 = "https://t.me/esenia_sergeeva"
#     link3 = "https://1drv.ms/w/s!Ag6XhthO_RvegV7R64K-SVsV_Xo1"
#
#     users = await CRUDUser.get_all()
#     for user in users:
#         tasks.append(bot.send_message(chat_id=user.user_id,
#                                       text=text,
#                                       reply_markup=await MainForms.gift(link=link, text="Ссылка на сайт")))
#
#         tasks2.append(bot.send_message(chat_id=user.user_id,
#                                        text=txt2,
#                                        reply_markup=await MainForms.gift(link=link2, text="Ссылка на мой тг")))
#
#         tasks3.append(bot.send_message(chat_id=user.user_id,
#                                        text=tasks3Text,
#                                        reply_markup=await MainForms.gift(link=link3, text="Рассрочка")))
#
#     await asyncio.gather(*tasks, return_exceptions=True)
#     await asyncio.gather(*tasks2, return_exceptions=True)
#     await asyncio.gather(*tasks3, return_exceptions=True)
#
#
# @dp.message_handler(IsAdmin(), commands=["8test"])  # в конце урока!!!
# async def registration_start8(message: types.Message):
#     text8 = "Спасибо всем, кто был онлайн❤️\n" \
#             "А для всех, кто не смог, мы сделали запись! Она доступна 24 часа🔥\n" \
#             "Было пушечно! ⬇️\n\n" \
#             "Код доступа: 9=*Qc*Xi"
#
#     tasks8 = []
#     link8 = "https://us02web.zoom.us/rec/share/c9swLy2xwyu6Hr9Yp-VGqUYyv1k44gjfRf-ZhoT-bm2MNEwo8IICEfVp0zLcH9IQ.QAfkhz9llykBEZGi"
#     users = await CRUDUser.get_all()
#     for user in users:
#         tasks8.append(bot.send_message(chat_id=user.user_id,
#                                        text=text8,
#                                        reply_markup=await MainForms.gift(link=link8,
#                                                                          text="Ссылка")))
#
#     await asyncio.gather(*tasks8, return_exceptions=True)


@dp.message_handler(IsAdmin(), commands=["texpod"])  # в конце урока!!!
async def registration_start8(message: types.Message):
    text8 = "Идентификатор конференции: 825 5638 3687\n" \
            "Код доступа: 860148\n\n" \
            "Техническая поддержка ➡️ https://t.me/sshlyomina"

    tasks8 = []
    link8 = "https://us02web.zoom.us/j/82556383687?pwd=V1VmMkgyQlpEQUxxUXpKRU0xYWpRUT09"
    users = await CRUDUser.get_all()
    for user in users:
        tasks8.append(bot.send_message(chat_id=user.user_id,
                                       text=text8,
                                       reply_markup=await MainForms.gift(link=link8,
                                                                         text="Ссылка на вход")))

    await asyncio.gather(*tasks8, return_exceptions=True)


@dp.message_handler(IsAdmin(), commands=["doc"])  # в конце урока!!!
async def registration_start8(message: types.Message):
    text8 = "Чтобы получить подробности о рассрочке, нажми сюда⬇"

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
