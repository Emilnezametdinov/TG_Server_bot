import logging
import asyncio
import aiogram

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from config import BOT_TOKEN, ADMIN_ID

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(msg: Message):
    await msg.answer(
        f'Привет, {msg.from_user.first_name}.\n'
        'Я - бот, который спрашивает всех про загрузку на день.\n'
        'Каждое утро я буду отправлять тебе напоминалку, чтобы ты записал мне свою загрузку.\n'
        'Отправь мне комманду /new и я запишу твою загрузку на день.'
        )

@dp.message(Command("new"))
async def New(msg: Message, loads: list):
    #loads.append(msg.text)
    #await msg.answer('Добавлена запись')
    await msg.answer('Ответ на /new')


@dp.message()
async def any_message(msg: Message):
    await msg.answer(
        f'Привет, {msg.from_user.first_name}.\n'
        'Это тестовый ответ на любое сообщение'
    )

'''
@dp.message(Command("show_list"))
async def cmd_show_list(msg: Message, mylist: list):
    await msg.answer(f"Ваш список: {mylist}")
'''










async def send_start_message():
    await bot.send_message(chat_id= ADMIN_ID, text='Bot started!')

async def main():
    await send_start_message()
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())