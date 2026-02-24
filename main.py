import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from bot.config import settings
from bot.db.db import rd


async def main():
    bot = Bot(token=settings.TOKEN)
    redis = RedisStorage(redis=rd)
    dp = Dispatcher(storage=redis)
    
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    asyncio.run(main())

