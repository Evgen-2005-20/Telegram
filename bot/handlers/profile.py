from aiogram import Router, F
from aiogram.types import Message

from bot.db.db import rd
from bot.db.logic_db import RedisDataBase


router = Router()
database = RedisDataBase(redis_client=rd)

@router.message(F.text == "/profile")
async def get_profile(message: Message):
    result = await database.get_user(message.from_user.id)

    if result:
        text = (
            f"Hi {result['username']}\n\n"
            f"Username: {result['username']}\n"
            f"Email: {result['email']}\n"
            f"Balance: {result['balance']}\n"
            f"Phone: {result['number']}"
        )

        await message.answer(text)
    else:
        await message.answer("Sorry, but you are not registered.")