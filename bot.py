import asyncio
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types

bot = Bot('8025131403:AAGFSmTIO5do4UXS5_kWWdsNXr7trpS3Plo')
dp = Dispatcher()

@dp.message(Command("start"))
async def echo(message: types.message):
    await message.answer(text='Hello')

@dp.message(Command("alina"))
async def alinaTraktor(message: types.message):
    await message.reply(text='TRACTOR')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
