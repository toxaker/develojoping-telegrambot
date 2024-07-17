import os
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler
from dotenv import load_dotenv

# Загрузка токена из .env файла
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Этапы и состояния для ConversationHandler
MENU_ACTION = range(1)

# Кнопки главного меню
main_menu_buttons = [
    [KeyboardButton('Главное меню')],
    [KeyboardButton('Помощь')]
]

# Функция для отправки главного меню
def send_main_menu(update: Update) -> None:
    menu_text = "<b>Главное меню:</b>"
    update.message.reply_text(menu_text, reply_markup=ReplyKeyboardMarkup(main_menu_buttons, resize_keyboard=True), parse_mode='HTML')

# Функция для команды /start
def start(update: Update, context: CallbackContext) -> int:
    welcome_text = 'Привет! Я ваш бот. Введите или нажмите "/help", чтобы увидеть доступные команды.'
    update.message.reply_text(welcome_text)
    send_main_menu(update)
    return MENU_ACTION

# Функция для команды /helpp
def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Доступные команды:\n"
        "/start - Начать взаимодействие с ботом\n"
        "/help - Показать это сообщение"
    )
    update.message.reply_text(help_text)

def main() -> None:
    # Создаем Updater и Dispatcher
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Добавляем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()