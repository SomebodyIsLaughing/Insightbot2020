from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
import keyboards as kb


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Клавиатура - stop
@dp.message_handler(commands=['stop'])
async def process_command_1(message: types.Message):
    await message.reply("Сейл, помни! Нет сделок - нет проблем!", reply_markup=kb.inline_kb1)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
