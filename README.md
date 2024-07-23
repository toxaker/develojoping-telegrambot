# Develojoping project
## My first steps to IT sphere. Telegram bot python based.

In the context of the profile as a whole, the "develojoping-ment" can be seen as a rough draft, for now, even if it may not follow the best approach completely. But this is not a big issue as long as the end result is not greatly affected. This initial section is dedicated to comprehending not only the programs and the code itself, but also, in principle, the underlying platforms and mechanisms of operation. After all, this is the first project, I was just learning and figuring things out. to repeat at my own risk, although mine are few if not none - after this short introduction, I attach all the materials that I have relied on and used. To be honest, there is more info than even needs for beginning, just be patient and attentive, and especially to these particularly helpful sources (libs and step-by-step tutorials).

https://github.com/python-telegram-bot/python-telegram-bot; https://github.com/eternnoir/pyTelegramBotAPI; https://github.com/kill26real/chat.

Also worth to visit https://core.telegram.org/api#bot-api; https://en.wikipedia.org/wiki/Telegram_(software); https://core.telegram.org/bots. its a BASE.

# Telegram Bot as web assistant, contact and consult helper for the web site.

## Introduction

This project is a Telegram bot written in Python. 
The resources used in the development are standard - BOT API, python-telegram-bot.
The initial idea was to realize the possibility of quick and convenient communication with me directly through the site, which would make it easier for a potential customer to make a purchase/receive information/receive answers to questions, etc., which in general would have a positive impact on the communication device as a whole (which can and does have a positive impact on the commercial side of the project (if it is commercial). For me, as an implementer, it would also simplify communication with the client due to the possibility of communicating in the most comfortable and accessible way.

However, during the development process, ideas and the opportunity to implement a number of other features came up, some of which are listed below and have already been implemented, in the debugging and soon-to-be-launched or under development phase.

## Functionality:

1. Contact with a potential client, meet and greet, bot description and instructions for use.
2. Providing basic information, frequently asked questions (assorted) and answers.
3. Contact information and contacts for complaints/suggestions/cooperation.
4. Range of services and price list.
5. Documentation and licenses.
6. Social links for contact with people and self-promotion.
7. Custom 'Menu' button, which is linked to website's main page.


##How it looks

I will provide a couple of screenshots to demonstarate at least how it looks, and main menu as basic functions (It's will be in Russian).

![startUI](https://github.com/user-attachments/assets/40362ac3-d551-46bc-b7d5-50022aa3180a)
User's start interface.


![mainmenu](https://github.com/user-attachments/assets/12846811-3f48-4d9c-a779-f34332913b0c)
Main menu with basic functions:
1. INFO
2. About bot
3. Question - user writes any message and bot is forwarding it directly to my telegram's
4. FAQ - 10 answers, mainly to give user a rewiew about what my website is and what i can do (stil have to work on content)
5. Social media's links - my main social pages
6. Services - currently, still working on it, but more likely will end soon.

Nothing extraordinary - but, that was my first, and i am not gonna lie - that was hard as fk. i almost lost patience a few times.
But now i am sure, it is just my beggining, and futher - more. Thanks everyone for the attention!

### CODE TIME !!!

#1. Lets start from the easiest thing ever:

1.1. Get python, if you still does not have it. My advice - from python.org is a way more comfortable (i did try from microsoft store also); I have python 3.12.4.
1.2. Not nesseceary - get the more 'modern' app for coding. I did choose Visual Studio Code - just because i am beginner - even this thing was not so easy to use for the first couple days.
1.3. Check out if you have installed your python correctly - 
python --version (via embeded terminal or windowses one - does not matter)
1.4. If you see red mistakes - you should try better, but if not - you are good to go futher. 'cd your_project_folder' - it will move you to your's work folder, where all your files will be.
1.5. Enviroment - actually it is not neccseary but i think you'd better to set it - it will help to avoid any versions of pips or even python's conflicts.

python -m venv venv

venv\Scripts\activate

first one to create, second to activate - if you did everything right - you will see your interface sligtly changed. It means you are ready.

#2. Requirements and pips

2.1 create a text file in your project's folder, .txt and write libs and pips you need to start. In my case it is:

python-telegram-bot
python-dotenv

2.2. upgrade those things if you been asked to. next step is creating .env file - it is file for your token - to not publish it, or constantly insert to code. If you have no idea what token is - bro, start from telegram's official docs, i left links earlier

2.3. Create your bot's file, for example

python-tg_bot.py

2.4. Well done. You should see something similiar in your work's folder:

![image](https://github.com/user-attachments/assets/760520f6-10fd-418b-a7b4-342baf4668bf)

2.5. I have done the whole code in a single file - except .env and reqs. But you can separate, for example level.py, format.py, config.py and etc

#3 Lets get it started

3.1. after you ensure you are in the folder you need:

pip install -r requirements.txt (or pip install python-telegram-not, python-dotenv, etc)

3.2. time for our bot. i will show basic steps, evrything following you got to figure out by yourself (take a look to my repositories files)

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

if TOKEN:
    print(f"Токен успешно загружен: {TOKEN[:5]}...")  # Показываем только первые 5 символов токена
else:
    print("Токен не загружен! Проверьте файл .env")
(ensuring message if you have your token loaded)

import logging

level=logging.INFO

(logging)

format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

ConversationHandler
MENU_ACTION, ASK_FAQ, ADMIN_AUTH, ADMIN_SECTION, MESSAGE_FORWARD = range(5)

<your code here :)>
few ideas:
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

    menu_text = "<b>Главное меню:</b>"
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=menu_text, 
        reply_markup=InlineKeyboardMarkup(formatted_buttons), 
        parse_mode='HTML'
    )

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE)

    async def info(update: Update, context: ContextTypes.DEFAULT_TYPE)

    async def about_me(update: Update, context: ContextTypes.DEFAULT_TYPE)

and etc, you got it!

aaand in the end:

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


#4 Good job! Wish you luck, my friend.



Questions to me personally?
buildon.python742@dralias.com
