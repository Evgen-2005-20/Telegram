from aiogram import Router, F
from aiogram.types import Message

from bot.keyboards.menu import main_menu

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message : Message):
    await message.answer(
        text=f"Hello {message.from_user.first_name} I'm a bot for working with finances. How can I help?",
        reply_markup=main_menu())

