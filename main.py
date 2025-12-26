import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# ВСТАВЬ СВОИ ДАННЫЕ СЮДА
TOKEN = "8215902516:AAE153xLFm7l75g--FXiXNu2drwg-3YclxI"
MY_PROFILE_LINK = "https://t.me/Na4lenax"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(f"Бог телеграмма: {MY_PROFILE_LINK}")

async def main():
    print("Бот запущен и готов к работе...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
