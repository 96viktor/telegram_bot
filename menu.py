import telegram
from key_buttons import tele_button, courses

def main_menu_keyboard():
    keyboard = ([
        [telegram.KeyboardButton(tele_button[0]),],
        [telegram.KeyboardButton(tele_button[1]),],
        [telegram.KeyboardButton(tele_button[2]),],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )
def courses_menu_keyboard():
    keyboard = ([
        [telegram.KeyboardButton(courses[0]),],
        [telegram.KeyboardButton(courses[1]),],
        [telegram.KeyboardButton(courses[2]),],
        [telegram.KeyboardButton(courses[3]),],
        [telegram.KeyboardButton(courses[4]),],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )
