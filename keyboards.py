from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# bots buttons
inline_btn_1 = InlineKeyboardButton('Welcome to INSIGHT', callback_data='button1', url='https://app.gitbook.com/@anton-kyrylenko/s/insight-2020/')
inline_btn_2 = InlineKeyboardButton('Общий FAQ', callback_data='button2', url='https://app.gitbook.com/@anton-kyrylenko/s/insight-2020/faq/digital-netapp-insight-2020')
inline_btn_3 = InlineKeyboardButton('Инструкция к посещению', callback_data='button3', url='https://app.gitbook.com/@anton-kyrylenko/s/insight-2020/faq/instrukciya-po-posesheniyu')
inline_btn_4 = InlineKeyboardButton('Сертификация и экзамены', callback_data='button4', url='https://app.gitbook.com/@anton-kyrylenko/s/insight-2020/faq/sertifikaciya')
inline_btn_5 = InlineKeyboardButton('Сессии, которые стоит посетить', callback_data='button5', url='https://app.gitbook.com/@anton-kyrylenko/s/insight-2020/sessions/sessyi')
inline_btn_6 = InlineKeyboardButton('Регистрация', callback_data='button6', url='https://insightregistration.netapp.com/flow/netapp/insightdigital/Reg/login')
inline_btn_7 = InlineKeyboardButton('Агенда', callback_data='button7', url='https://insight.netapp.com/agenda/')
inline_btn_8 = InlineKeyboardButton('Полный каталог сессий', callback_data='button8', url='https://insight.netapp.com/sessions/?#/')
inline_kb1 = InlineKeyboardMarkup(row_width=1).add(inline_btn_1,inline_btn_2,inline_btn_3,inline_btn_4,inline_btn_5,inline_btn_6,inline_btn_7,inline_btn_8)


