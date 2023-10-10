from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import TOKEN
from menu import (
    main_menu_keyboard,
    courses_menu_keyboard
)
from key_buttons import tele_button, courses


ABOUT = tele_button[0]
COURSES = tele_button[1]
WHERE_ARE_WE = tele_button [2]
PYTHON = courses[0]
JAVA = courses [1]
JS = courses [2]
QA = courses [3]
BACK = courses [4]

def start(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Добро пожаловать {update.effective_user.username}\nэтот бот поможет вам с информацией о курсах',
        reply_markup=main_menu_keyboard()
    )


def about(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Преимущества обучения в Codify · Обучение с нуля до Junior. Пройди обучение по авторской программе Codify и стань Junior специалистом.\nsite:\nhttps://www.codifylab.com/'
    )
    
def reply_courses(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Choose course',
        reply_markup=courses_menu_keyboard()
    )
    
def reply_python(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией' 
        'и автоматическим управлением памятью, ориентированный на повышение производительности разработчика,'
        'читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ.'
    )

def reply_java(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Java — строго типизированный объектно-ориентированный язык программирования общего назначения,' 
        'разработанный компанией Sun Microsystems. Разработка ведётся сообществом, организованным через' 
        'Java Community Process; язык и основные реализующие его технологии распространяются по лицензии GPL'
    )

def reply_js(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'JavaScript — мультипарадигменный язык программирования. Поддерживает объектно-ориентированный,' 
        'императивный и функциональный стили. Является реализацией спецификации ECMAScript. JavaScript' 
        'обычно используется как встраиваемый язык для программного доступа к объектам приложений.'
    )

def reply_qa(update:Update,context:CallbackContext):
    update.message.reply_text(
        f'Обеспечение качества — это процесс или результат формирования требуемых свойств и характеристик' 
        'продукции по мере её создания, а также — поддержание этих характеристик при хранении, транспортировани'
        'и эксплуатации продукции. Обеспечение качества определено в стандарте ISO 9000:2005 «Системы менеджмента'
        'качества'
    )

def reply_back(update: Update, context: CallbackContext):
    update.message.reply_text(
        f'Вы вернулись в главное меню.',
        reply_markup=main_menu_keyboard()
    )

def where_are_we(update:Update, context:CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'Location of Codify'
    )
    update.message.reply_location(
        #42.82909025000069, 74.61687279022618
        longitude=74.61687279022618,
        latitude=42.82909025000069,
        reply_to_message_id=msg.message_id
    )


updater = Updater(token=TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(WHERE_ARE_WE),
    where_are_we
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSES),
    reply_courses
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    reply_python
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JAVA),
    reply_java
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS),
    reply_js
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(QA),
    reply_qa
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    reply_back
))

updater.start_polling()
updater.idle()