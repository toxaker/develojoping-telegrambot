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
        [InlineKeyboardButton('Информация', callback_data='info')],         [InlineKeyboardButton('FAQ', callback_data='faq')],
        [InlineKeyboardButton('Вебсайт', url='https://iamtoxakalinin.ru')],         [InlineKeyboardButton('Соц.сети', callback_data='social_media')],
        [InlineKeyboardButton('Родителям', callback_data='parents')],       [InlineKeyboardButton('Вопрос?', callback_data='question')],

        [InlineKeyboardButton('Обо мне', callback_data='about_me')],
    ]
    menu_text = "<b>Главное меню:</b>"
    update.message.reply_text(menu_text, reply_markup=InlineKeyboardMarkup(main_menu_buttons), parse_mode='HTML')

# Функция для команды /start
def start(update: Update, context: CallbackContext) -> int:
    welcome_text = 'Привет! Я тохабот. Введите или нажмите "/help", чтобы увидеть доступные команды.'
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
        "Вебсайт - Перейти на сайт\n"
        "Родителям - Доступ для родителей\n"
        "Обо мне - Информация об авторе\n"
        "Соц.сети - Ссылки на социальные сети\n"
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

# Функция для вебсайта (InlineKeyboardButton с URL уже добавлен в send_main_menu)

# Функция для раздела Родителям
def parents(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Пожалуйста, введите вашу дату рождения (ДД.ММ.ГГГГ):')
    return PARENTS_AUTH

# Обработка даты рождения
def parents_auth(update: Update, context: CallbackContext) -> int:
    bday = update.message.text
    # Здесь должна быть логика проверки даты рождения
    # Например, если дата совпадает с базой данных
    allowed_dates = 0606.2001, 1607.1979, 2605.1977, 1006.1976, 0604.2010, 31.01, 31082001  # Пример дат в базе данных
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
        [InlineKeyboardButton('GITHUB', url='https://github.com/toxakalinin')],
        [InlineKeyboardButton('Mastodon', url='https://mastodon.social/@toxakalinin')],
        [InlineKeyboardButton('X', url='https://x.com/toxakalinin/')],
    ]
    update.message.reply_text('Мои социальные сети:', reply_markup=InlineKeyboardMarkup(social_buttons))

# Функция для пересылки вопроса
def question(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Пожалуйста, введите ваш вопрос:')
    return MESSAGE_FORWARD

def forward_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    # ID вашего чата в Телеграме, куда будут пересылаться сообщения
    chat_id = 1010101010
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

def main() -> None:
    # Создаем Updater и Dispatcher
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Добавляем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("info", info))

    # Обработчик инлайн-кнопок
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Обработчик сообщений (для пересылки вопросов)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))

    # Добавляем ConversationHandler для раздела "Родителям"
    parents_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(parents, pattern='^parents$')],
        states={
            PARENTS_AUTH: [MessageHandler(Filters.text & ~Filters.command, parents_auth)],
            PARENTS_SECTION: [CallbackQueryHandler(parents_section, pattern='^parents_section$')]
        },
        fallbacks=[CallbackQueryHandler(back, pattern='^back$')]
    )
    dispatcher.add_handler(parents_handler)

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
