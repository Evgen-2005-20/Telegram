from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.text == "balance")
async def balance_handler(callback : CallbackQuery):
    pass