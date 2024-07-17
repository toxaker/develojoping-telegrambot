import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler, ConversationHandler
from dotenv import load_dotenv

# Загрузка токена из .env файла
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Этапы и состояния для ConversationHandler
MENU_ACTION, PARENTS_AUTH, PARENTS_SECTION, MESSAGE_FORWARD = range(4)

# Функция для отправки главного меню
def send_main_menu(update: Update) -> None:
    main_menu_buttons = [
        [InlineKeyboardButton('Информация', callback_data='info')],
        [InlineKeyboardButton('FAQ', callback_data='faq')],
        [InlineKeyboardButton('Обратная связь', callback_data='feedback')],
        [InlineKeyboardButton('Родителям', callback_data='parents')],
        [InlineKeyboardButton('Обо мне', callback_data='about_me')],
        [InlineKeyboardButton('Соц.сети', callback_data='social_media')],
        [InlineKeyboardButton('Услуги', callback_data='services')],
        [InlineKeyboardButton('Вопрос?', callback_data='question')],
        [InlineKeyboardButton('Назад', callback_data='back')]
    ]
    menu_text = "<b>Главное меню:</b>"
    update.message.reply_text(menu_text, reply_markup=InlineKeyboardMarkup(main_menu_buttons), parse_mode='HTML')

# Функция для команды /start
def start(update: Update, context: CallbackContext) -> int:
    welcome_text = 'Привет! Я ваш бот. Введите или нажмите "/help", чтобы увидеть доступные команды.'
    update.message.reply_text(welcome_text)
    send_main_menu(update)
    return MENU_ACTION

# Функция для команды /help
def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Доступные команды:\n"
        "/start - Начать взаимодействие с ботом\n"
        "/help - Показать это сообщение\n"
        "/info - Информация о боте\n"
        "FAQ - Часто задаваемые вопросы\n"
        "Обратная связь - Оставить отзыв или сообщить\n"
        "Родителям - Доступ для родителей\n"
        "Обо мне - Информация об авторе\n"
        "Соц.сети - Ссылки на социальные сети\n"
        "Услуги - Информация об услугах\n"
        "Вопрос? - Задать вопрос\n"
        "Назад - Вернуться в главное меню"
    )
    update.message.reply_text(help_text)

# Функция для команды /info
def info(update: Update, context: CallbackContext) -> None:
    info_text = "Этот бот предоставляет информацию и помощь по различным вопросам. Вы можете узнать больше, выбрав соответствующие пункты меню."
    update.message.reply_text(info_text)

# Функция для FAQ
def faq(update: Update, context: CallbackContext) -> None:
    faq_buttons = [
        [InlineKeyboardButton('Вопрос 1', callback_data='faq_1')],
        [InlineKeyboardButton('Вопрос 2', callback_data='faq_2')],
        [InlineKeyboardButton('Вопрос 3', callback_data='faq_3')],
        [InlineKeyboardButton('Назад', callback_data='back')]
    ]
    update.message.reply_text('Выберите вопрос:', reply_markup=InlineKeyboardMarkup(faq_buttons))

# Функция для обратной связи
def feedback(update: Update, context: CallbackContext) -> None:
    feedback_buttons = [
        [InlineKeyboardButton('Отзыв', url='https://iamtoxakalinin.ru/reviews')],
        [InlineKeyboardButton('Сообщить', callback_data='report')],
        [InlineKeyboardButton('Назад', callback_data='back')]
    ]
    update.message.reply_text('Выберите действие:', reply_markup=InlineKeyboardMarkup(feedback_buttons))

# Функция для "Сообщить" в разделе обратной связи
def report(update: Update, context: CallbackContext) -> None:
    report_text = (
        "Вы можете связаться со мной следующими способами:\n"
        "- Email: example@example.com (для деловых предложений)\n"
        "- Телеграм: @example (для быстрого ответа)\n"
        "Выберите наиболее удобный для вас способ."
    )
    update.message.reply_text(report_text)

# Функция для раздела "Родителям"
def parents(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Пожалуйста, введите вашу дату рождения (ДД.ММ.ГГГГ):')
    return PARENTS_AUTH

# Обработка даты рождения
def parents_auth(update: Update, context: CallbackContext) -> int:
    bday = update.message.text
    # Здесь должна быть логика проверки даты рождения
    # Например, если дата совпадает с базой данных
    allowed_dates = ['01.01.2000', '02.02.2001']  # Пример дат в базе данных
    if bday in allowed_dates:
        update.message.reply_text('Доступ разрешен.')
        parents_section(update, context)
    else:
        update.message.reply_text('Доступ запрещен.')
        send_main_menu(update)
    return MENU_ACTION

# Функция для раздела после успешной аутентификации
def parents_section(update: Update, context: CallbackContext) -> None:
    parents_menu_buttons = [
        [InlineKeyboardButton('Маме', callback_data='mom')],
        [InlineKeyboardButton('Сереже', callback_data='sergey')],
        [InlineKeyboardButton('Назад', callback_data='back')]
    ]
    update.message.reply_text('Добро пожаловать в раздел для родителей! Чем могу помочь?', reply_markup=InlineKeyboardMarkup(parents_menu_buttons))

# Функция для информации об авторе
def about_me(update: Update, context: CallbackContext) -> None:
    about_text = "Автор этого бота - Тоха Калинин."
    update.message.reply_text(about_text)

# Функция для соц.сетей
def social_media(update: Update, context: CallbackContext) -> None:
    social_buttons = [
        [InlineKeyboardButton('ВКонтакте', url='https://vk.com')],
        [InlineKeyboardButton('Facebook', url='https://facebook.com')],
        [InlineKeyboardButton('Instagram', url='https://instagram.com')]
    ]
    update.message.reply_text('Мои социальные сети:', reply_markup=InlineKeyboardMarkup(social_buttons))

# Функция для пересылки вопроса
def question(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Пожалуйста, введите ваш вопрос:')
    return MESSAGE_FORWARD

def forward_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    # ID вашего чата в Телеграме, куда будут пересылаться сообщения
    chat_id = 123456789
    context.bot.send_message(chat_id=chat_id, text=user_message)
    update.message.reply_text('Ваш вопрос отправлен.')

# Функция для кнопки Назад
def back(update: Update, context: CallbackContext) -> None:
    send_main_menu(update)

# Обработка callback_data из инлайн-кнопок
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'info':
        info(query, context)
    elif query.data == 'faq':
        faq(query, context)
    elif query.data == 'feedback':
        feedback(query, context)
    elif query.data == 'report':
        report(query, context)
    elif query.data == 'parents':
        parents(query, context)
    elif query.data == 'mom':
        update.callback_query.message.reply_text('Раздел для мамы. Чем могу помочь?', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('На Главную', callback_data='back')]]))
    elif query.data == 'sergey':
        update.callback_query.message.reply_text('Раздел для Сереже. Чем могу помочь?', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('На Главную', callback_data='back')]]))
    elif query.data == 'about_me':
        about_me(query, context)
    elif query.data == 'social_media':
        social_media(query, context)
    elif query.data == 'question':
        question(query, context)
    elif query.data == 'back':
        back(query, context)
    elif query.data == 'services':
        services(query, context)
    elif query.data == 'price':
        price(query, context)
    elif query.data == 'types':
        types(query, context)

# Функция для раздела "Услуги"
def services(update: Update, context: CallbackContext) -> None:
    services_buttons = [
        [InlineKeyboardButton('Прайс', callback_data='price')],
        [InlineKeyboardButton('Виды', callback_data='types')],
        [InlineKeyboardButton('Назад', callback_data='back')]
    ]
    update.message.reply_text('Выберите действие:', reply_markup=

InlineKeyboardMarkup(services_buttons))

# Функция для раздела "Прайс"
def price(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Прайс услуг.')

# Функция для раздела "Виды"
def types(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Виды услуг.')

def main() -> None:
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Определение ConversationHandler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            MENU_ACTION: [
                CallbackQueryHandler(button),
                CommandHandler('help', help_command)
            ],
            PARENTS_AUTH: [
                MessageHandler(Filters.text & ~Filters.command, parents_auth)
            ],
            MESSAGE_FORWARD: [
                MessageHandler(Filters.text & ~Filters.command, forward_message)
            ]
        },
        fallbacks=[CommandHandler('start', start)]
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CommandHandler('help', help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()