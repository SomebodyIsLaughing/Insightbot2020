from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# bots buttons
inline_btn_1 = InlineKeyboardButton('Уголок Stop Managera', callback_data='button1', url='https://sales.antonkyrylenko.tech/')
inline_btn_2 = InlineKeyboardButton('Бандлы', callback_data='button2', url='https://sales.antonkyrylenko.tech/express-packs')
inline_btn_3 = InlineKeyboardButton('Календарь ДЕМО', callback_data='button3', url='https://calendar.google.com/calendar/u/0?cid=azgxamtwazJsaXN2NWlidjdqOWRuMGFxM29AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ')
inline_btn_4 = InlineKeyboardButton('Конфигурация ДЕМО', callback_data='button4', url='https://docs.google.com/spreadsheets/d/1alJqdJHFRAFoMW_F_kARS5cn-AU-4vn-5k426g4ozyA/edit#gid=0')
inline_btn_5 = InlineKeyboardButton('Опросник СХД', callback_data='button5', url='https://forms.gle/z5JQeaU4zZTC9mbR6')
inline_btn_6 = InlineKeyboardButton('Опросник Видеонаблюдение', callback_data='button6', url='https://forms.gle/6RN3ndGnfzaK8RKG9')
inline_btn_7 = InlineKeyboardButton('Форма регистраии', callback_data='button7', url='https://forms.gle/KMDKTmqYQTbr6KW49')
inline_kb1 = InlineKeyboardMarkup(row_width=1).add(inline_btn_1,inline_btn_2,inline_btn_3,inline_btn_4,inline_btn_5,inline_btn_6,inline_btn_7)


