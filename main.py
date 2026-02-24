import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from bot.config import settings
from bot.db.db import rd
from bot.handlers import start, register
from bot.middlewares import typing


async def main():
    bot = Bot(token=settings.TOKEN)
    redis = RedisStorage(redis=rd)
    dp = Dispatcher(storage=redis)
    
    dp.message.middleware(typing.TypingMessage())
    
    dp.include_router(start.router)
    dp.include_router(register.router)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await rd.close()
    
    
if __name__ == "__main__":
    asyncio.run(main())

