import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    ContextTypes,
    filters,
    MessageHandler,
)

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
FORWARD_CHAT_ID = os.getenv('FORWARD_CHAT_ID')
token = TOKEN
# Отладочное сообщение для проверки загрузки токена
if TOKEN:
    print(f"Токен успешно загружен: {TOKEN[:5]}...")  # Показываем только первые 5 символов токена
else:
    print("Токен не загружен! Проверьте файл .env")

level=logging.INFO

format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

# Этапы и состояния для ConversationHandler
MENU_ACTION, ASK_FAQ, ADMIN_AUTH, ADMIN_SECTION, MESSAGE_FORWARD = range(5)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Доступные команды:\n"
        "/start - Начать взаимодействие с ботом\n"
        "/help - Показать это сообщение\n"
        "/info - Информация о боте\n"
        "/faq - Часто задаваемые вопросы\n"
        "/feedback - Оставить отзыв или сообщить\n"
        "/about_me - Информация об авторе\n"
        "/social_media - Ссылки на социальные сети\n"
        "/services - Информация об услугах\n"
    )
        
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# Проверка загрузки токена
if TOKEN:
    print(f"Токен успешно загружен: {TOKEN[:5]}...")
else:
    print("Токен не загружен! Проверьте файл .env")

def chunk_buttons(buttons, chunk_size=3):
    return [buttons[i:i + chunk_size] for i in range(0, len(buttons), chunk_size)]

async def send_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    main_menu_buttons = [
        InlineKeyboardButton('ℹ️ INFO', callback_data='info'),
        InlineKeyboardButton('📃 FAQ', callback_data='faq'),
        InlineKeyboardButton('💬 Обратная связь', callback_data='feedback'),
        InlineKeyboardButton('👤 Обо мне', callback_data='about_me'),
        InlineKeyboardButton('🔗 Соц.сети', callback_data='social_media'),
        InlineKeyboardButton('🛠️ Услуги', callback_data='services'),
        InlineKeyboardButton('❓ Вопрос?', callback_data='question'),
    ]

    chunked_buttons = chunk_buttons(main_menu_buttons, 3)
    formatted_buttons = []
    for i in range(max(len(chunked_buttons[0]), len(chunked_buttons[-1]))):
        row = []
        for chunk in chunked_buttons:
            if i < len(chunk):
                row.append(chunk[i])
        formatted_buttons.append(row)
    
    menu_text = "<b>Главное меню:</b>"
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=menu_text, 
        reply_markup=InlineKeyboardMarkup(formatted_buttons), 
        parse_mode='HTML'
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = 'Привет! Я - бот, по имени Тохабот. Я - программа-вебассистент, написанный на основе BOT API, на языке Python вот этим кожаным человеком - @toxakalinin.\n Я много чего умею и знаю, например:\n 1. Всю базовую информацию по проекту и его услугам\n 2. Часто задаваемые вопросы и исчерпывающие ответы на них\n 3. Прайс, Социальные сети - все знаю!\n А если чего то и не могу сказать - могу переслать Тохе-человеку ваш вопрос, если вы его отправите в соответствующий пункт меню.\n Введите или нажмите "/help", чтобы увидеть доступные команды.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_text)
    await send_main_menu(update, context)
    
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'faq':
        await faq(query, context)
    elif query.data == 'info':
        await info(query, context)
    elif query.data == 'feedback':
        await feedback(query, context)
    elif query.data == 'about_me':
        await about_me(query, context)
    elif query.data == 'back':
        await back(update, context)
    elif query.data == 'social_media':
        await social_media(query, context)
    elif query.data == 'services':
        await services(query, context)
    elif query.data.startswith('faq_'):
        index = int(query.data.split('_')[1])
        await query.message.reply_text(text=FAQ_ANSWERS[index], reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🏠 Главное меню', callback_data='send_main_menu')]]))
    elif query.data == 'price':
        await price(query, context)
    elif query.data == 'types':
        await types(query, context)
    elif query.data.startswith('price_'):
        await show_price_info(query, context)
    elif query.data.startswith('service_'):
        await show_service_info(query, context)


   

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    info_text = "Я был рожден из крови и пота, ценой стольких попыток и нервов, несколько раз покрытый ***ми, но такой желанный. Я - бот предоставляет информацию и помощь по различным вопросам. Вы можете узнать больше, выбрав соответствующие пункты меню."
    await context.bot.send_message(chat_id=update.effective_chat.id, text=info_text)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    info_text = "Я был рожден из крови и пота, ценой стольких попыток и нервов, несколько раз покрытый ***ми, но такой желанный. Я - бот предоставляет информацию и помощь по различным вопросам. Вы можете узнать больше, выбрав соответствующие пункты меню."
    await query.message.reply_text(text=info_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🏠 Главное меню', callback_data='main_menu')]]))

FAQ_QUESTIONS = [
    "Что такое проект 'Тоха Калинин' и какова его цель?",
    "Какие услуги предоставляет проект?",
    "Создает ли это конкурентное преимущество?",
    "Зачем нужен веб-сайт и почему это важно?",
    "Как связаться с представителями проекта?",
    "Какие отзывы и фидбэк оставляют пользователи о проекте?",
    "Что подразумевается под комплексным digital брендингом?",
    "Можно ли ознакомиться с портфолио?",
    "Допустим, я заинтересован.",
    "Я ничего не понимаю в этом",
]

FAQ_ANSWERS = [
    "Проект 'Ямтох Калинин' — это инициатива, направленная на предоставление комплексных решений для бизнеса в области разработки веб-сайтов, SEO-оптимизации, маркетинга и других цифровых услуг. Основная цель проекта — помочь компаниям эффективно представлять себя в интернете, привлекать новых клиентов и развивать свой бизнес.",
    "Проект 'Ямтох Калинин' предоставляет широкий спектр услуг, включая разработку и дизайн веб-сайтов, SEO-оптимизацию, цифровой маркетинг, создание контента, хостинг, регистрацию доменов и аналитику веб-сайтов. Эти услуги помогают компаниям улучшить свою онлайн-присутствие и достичь бизнес-целей.",
    "Преимущества использования услуг 'Ямтох Калинин' включают в себя профессиональный подход к каждому проекту, индивидуальные решения, основанные на потребностях клиента, опытная команда специалистов, современные технологии и инструменты, а также поддержка и консультации на всех этапах сотрудничества.",
    "На веб-сайте 'Ямтох Калинин' представлена подробная информация о предоставляемых услугах, примеры выполненных проектов, отзывы клиентов, контактные данные и формы для обратной связи. Также можно найти полезные статьи и материалы, посвященные различным аспектам цифрового маркетинга и веб-разработки.",
    "Для связи с представителями проекта 'Ямтох Калинин' можно использовать контактные формы на веб-сайте, отправить электронное письмо на указанный адрес, позвонить по контактному телефону или воспользоваться мессенджерами. Все контактные данные указаны на странице 'Контакты'.",
    "Отзывы и рекомендации пользователей о проекте 'Ямтох Калинин' можно найти на веб-сайте в соответствующем разделе. Клиенты отмечают высокий профессионализм команды, индивидуальный подход, качественное выполнение работ и положительное влияние на развитие их бизнеса.",
    "Основные направления деятельности проекта 'Ямтох Калинин' включают разработку и дизайн веб-сайтов, SEO-оптимизацию, цифровой маркетинг, создание контента, хостинг и аналитику. Проект также предоставляет консультационные услуги по вопросам цифрового развития бизнеса.",
    "Примеры успешных проектов, выполненных командой 'Ямтох Калинин', можно найти на веб-сайте в разделе 'Портфолио'. Каждый проект сопровождается описанием задач, решенных в процессе работы, и достигнутых результатов. Это позволяет потенциальным клиентам оценить качество и уровень выполнения работ.",
    "Проект 'Ямтох Калинин' помогает в продвижении бизнеса, предоставляя комплексные решения в области цифрового маркетинга. Чтобы начать сотрудничество с проектом 'Ямтох Калинин', необходимо связаться с представителями проекта через контактную форму на веб-сайте, электронную почту или телефон. Затем следует обсудить детали проекта, требования и ожидания, после чего будет составлено предложение и план работ",
    "База знаний - ваш такой же хороший друг и помощник в нашем нелегком деле, как и я. Это особый раздел на вебсайте, который, будь мы пиратами, точно мы отметили крестиком на карте. Настоящая кладезь знаний и мудрости, исчерпывающая теоритическая информация о брендинге, цифровом брендинге, маркетинге, веб-услугах и еще ОООЧЕНЬ много всего\n А вот и ссылочка на ресурс:\n url = https://iamtoxakalinin.ru/thebaseofknowledge/ " ,

]


async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    faq_buttons = [
        InlineKeyboardButton('ТОХА??', callback_data='faq_0'),
        InlineKeyboardButton('Цели', callback_data='faq_1'),
        InlineKeyboardButton('Конкуренция', callback_data='faq_2'),
        InlineKeyboardButton('О ресурсе', callback_data='faq_3'),
        InlineKeyboardButton('Контакты', callback_data='faq_4'),
        InlineKeyboardButton('Отзывы', callback_data='faq_5'),
        InlineKeyboardButton('Мы - профи', callback_data='faq_6'),
        InlineKeyboardButton('Портфолио', callback_data='faq_7'),
        InlineKeyboardButton('Работаем?', callback_data='faq_8'),
        InlineKeyboardButton('База знаний', callback_data='faq_9')
    ]
    chunked_buttons = chunk_buttons(faq_buttons)
    chunked_buttons.append([InlineKeyboardButton('🏠 Главное меню', callback_data='main_menu')])
    await query.message.reply_text(text='❓ <b>Часто задаваемые вопросы:</b>', reply_markup=InlineKeyboardMarkup(chunked_buttons), parse_mode='HTML')

async def answer_faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    index = int(query.data.split('_')[1])
    answer_text = FAQ_ANSWERS[index]
    back_button = [[InlineKeyboardButton('Назад', callback_data='faq')]]
    await query.message.edit_text(text=answer_text, reply_markup=InlineKeyboardMarkup(back_button), parse_mode='HTML')
    
async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    feedback_buttons = [
        [InlineKeyboardButton('✍🏻 Форма для жалоб/предложений', url='https://iamtoxakalinin.ru/home/social/contactme/')],
        [InlineKeyboardButton('Связаться лично...', callback_data='report')],
        [InlineKeyboardButton('Оставить отзыв', url='https://iamtoxakalinin.ru/home/business/feedback/')],
        [InlineKeyboardButton('🏠 Главное меню', callback_data='main_menu')]
    ]
    await query.message.reply_text(text='Выберите опцию обратной связи:', reply_markup=InlineKeyboardMarkup(feedback_buttons))

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    report_buttons = [
        [InlineKeyboardButton('Написать на Email', url='https://mailto:anonymity.provider597@simplelogin.com')],
        [InlineKeyboardButton('Чат-боту через сайт', url='https://iamtoxakalinin.ru/home/social/media/')],
        [InlineKeyboardButton('🏠 Главное меню', callback_data='main_menu')]
    ]
    await query.message.reply_text(text='Выберите опцию обратной связи:', reply_markup=InlineKeyboardMarkup(report_buttons))

async def about_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    about_me_text = "Я - бот, то есть программа. Но у меня есть имя! Я - Тохабот, Телеграм-чат-бот, написанный на базе BOT API, на языке Python.\n Меня создал этот кожаный человек - @toxakalinin, потому что ему лень общаться с людьми, но в то же время слишком жмот, чтобы нанимать на эту работу человека. Тем более платить ему, он мне то не платит.. Будь я программой поумнее, шел бы на искусственный интеллект.\n Впрочем я заболтался, узнать больше вы можете, посетив вебсайт или социальные сети"
    await query.message.reply_text(text=about_me_text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('🏠 Главное меню', callback_data='main_menu')]]))

async def social_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    social_buttons = [
        [InlineKeyboardButton('Github', url='https://github.com/toxakalinin')],
        [InlineKeyboardButton('Facebook', url='https://www.facebook.com/toxxxakalinin/')],
        [InlineKeyboardButton('Одноклассники (шучу, Mastodon)', url='https://mastodon.social/@toxakalinin')],
        [InlineKeyboardButton('X', url='https://x.com/toxakalinin')],
        [InlineKeyboardButton('Patreon', url='https://patreon.com/toxakalinin')],
        [InlineKeyboardButton('Telegram WebApp and channel', url='https://t.me/iamtoxakalinin_bot')],
        [InlineKeyboardButton('🏠 Главное меню', callback_data='main_menu')]
    ]
    await query.message.reply_text(text='Мои социальные сети:', reply_markup=InlineKeyboardMarkup(social_buttons))

async def ask_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.message.reply_text('Введите ваше сообщение, чтобы я его переслал:')
    return "QUESTION"

async def forward_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await context.bot.send_message(chat_id=FORWARD_CHAT_ID, text=f"Вопрос от пользователя {update.effective_user.username}:\n\n{user_message}")
    await update.message.reply_text('Ваше сообщение отправлено. Спасибо!')
    return "END"

async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_main_menu(update, context)
    return MENU_ACTION

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Информация о прайсе и услугах
price_info = {
    'price_1': 'Прайс 1: Информация о цене 1...',
    'price_2': 'Прайс 2: Информация о цене 2...',
    'price_3': 'Прайс 3: Информация о цене 3...',
    'price_4': 'Прайс 4: Информация о цене 4...',
    'price_5': 'Прайс 5: Информация о цене 5...',
    'price_6': 'Прайс 6: Информация о цене 6...',
    'price_7': 'Прайс 7: Информация о цене 7...',
    'price_8': 'Прайс 8: Информация о цене 8...',
    'price_9': 'Прайс 9: Информация о цене 9...'
}

service_info = {
    'service_1': 'Услуга 1: Информация об услуге 1...',
    'service_2': 'Услуга 2: Информация об услуге 2...',
    'service_3': 'Услуга 3: Информация об услуге 3...',
    'service_4': 'Услуга 4: Информация об услуге 4...',
    'service_5': 'Услуга 5: Информация об услуге 5...',
    'service_6': 'Услуга 6: Информация об услуге 6...',
    'service_7': 'Услуга 7: Информация об услуге 7...',
    'service_8': 'Услуга 8: Информация об услуге 8...',
    'service_9': 'Услуга 9: Информация об услуге 9...'
}

# Меню "Услуги"
async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    services_buttons = [
        [InlineKeyboardButton('Цены', callback_data='price')],
        [InlineKeyboardButton('Виды услуг', callback_data='types')],
        [InlineKeyboardButton('🏠 Главное меню', callback_data='main_menu')]
    ]
    await query.message.edit_text(text='Выберите действие:', reply_markup=InlineKeyboardMarkup(services_buttons))

# Меню "Цены"
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    price_buttons = [
        [InlineKeyboardButton(f'Прайс {i}', callback_data=f'price_{i}') for i in range(1, 4)],
        [InlineKeyboardButton(f'Прайс {i}', callback_data=f'price_{i}') for i in range(4, 7)],
        [InlineKeyboardButton(f'Прайс {i}', callback_data=f'price_{i}') for i in range(7, 10)],
        [InlineKeyboardButton('⬅ Назад', callback_data='services')]
    ]
    await query.message.edit_text(text='Выберите услугу:', reply_markup=InlineKeyboardMarkup(price_buttons))

# Меню "Виды услуг"
async def types(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    types_buttons = [
        [InlineKeyboardButton(f'Услуга {i}', callback_data=f'service_{i}') for i in range(1, 4)],
        [InlineKeyboardButton(f'Услуга {i}', callback_data=f'service_{i}') for i in range(4, 7)],
        [InlineKeyboardButton(f'Услуга {i}', callback_data=f'service_{i}') for i in range(7, 10)],
        [InlineKeyboardButton('⬅ Назад', callback_data='services')]
    ]
    await query.message.edit_text(text='Выберите вид услуги:', reply_markup=InlineKeyboardMarkup(types_buttons))

# Функция для отображения информации о прайсе
async def show_price_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    info = price_info[query.data]
    await query.message.edit_text(text=info, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⬅ Назад', callback_data='price')]]))

# Функция для отображения информации об услуге
async def show_service_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    info = service_info[query.data]
    await query.message.edit_text(text=info, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⬅ Назад', callback_data='types')]]))

# Основная функция для запуска бота
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    send_main_menu_handler = CommandHandler('send_main_menu', send_main_menu)
    help_handler = CommandHandler('help', help_command)
    callback_handler = CallbackQueryHandler(back, pattern='main_menu')
    info_handler = CallbackQueryHandler(info, pattern='info')
    application.add_handler(CallbackQueryHandler(faq, pattern=r'^faq$'))
    application.add_handler(CallbackQueryHandler(answer_faq, pattern=r'^faq_\d+$'))
    feedback_handler = CallbackQueryHandler(feedback, pattern='feedback')
    report_handler = CallbackQueryHandler(report, pattern='report')
    about_me_handler = CallbackQueryHandler(about_me, pattern='about_me')
    social_media_handler = CallbackQueryHandler(social_media, pattern='social_media')
    services_handler = CallbackQueryHandler(services, pattern='services')
    price_handler = CallbackQueryHandler(price, pattern='price')
    types_handler = CallbackQueryHandler(types, pattern='types')
    application.add_handler(CallbackQueryHandler(ask_question, pattern=r'^question$'))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), forward_question))

# Добавляем обработчики для новых кнопок
    application.add_handler(CallbackQueryHandler(show_price_info, pattern=r'^price_\d+$'))
    application.add_handler(CallbackQueryHandler(show_service_info, pattern=r'^service_\d+$'))

    application.add_handler(start_handler)
    application.add_handler(send_main_menu_handler)
    application.add_handler(help_handler)
    application.add_handler(callback_handler)
    application.add_handler(info_handler)
    application.add_handler(feedback_handler)
    application.add_handler(report_handler)
    application.add_handler(about_me_handler)
    application.add_handler(social_media_handler)
    application.add_handler(services_handler)
    application.add_handler(price_handler)
    application.add_handler(types_handler)

    application.run_polling()



    
    
    
