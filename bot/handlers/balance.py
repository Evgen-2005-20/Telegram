from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.db.logic_db import RedisDataBase
from bot.db.db import rd
from bot.keyboards.menu import balance_keyboard

router = Router()
db = RedisDataBase(rd)

@router.callback_query(F.data == "balance")
async def show_balance(callback: CallbackQuery):
    await callback.answer()

    user_id = callback.from_user.id
    user = await db.get_user(user_id)

    if not user:
        await callback.message.answer("User not found")
        return

    balance = int(user.get("balance", 0))

    await callback.message.answer(
        f"Your balance: {balance}$",
        reply_markup=balance_keyboard()
    )


@router.callback_query(F.data.startswith("deposit_"))
async def deposit_handler(callback: CallbackQuery):
    await callback.answer()

    user_id = callback.from_user.id
    amount = int(callback.data.split("_")[1])

    new_balance = await db.change_balance(user_id, amount)

    if new_balance is None:
        await callback.message.answer("User not found")
        return

    await callback.message.answer(
        f"Deposited {amount}$\n New balance: {new_balance}$"
    )


@router.callback_query(F.data.startswith("withdraw_"))
async def withdraw_handler(callback: CallbackQuery):
    await callback.answer()

    user_id = callback.from_user.id
    amount = int(callback.data.split("_")[1])

    user = await db.get_user(user_id)

    if not user:
        await callback.message.answer("User not found")
        return

    balance = int(user.get("balance", 0))

    if balance < amount:
        await callback.message.answer("Not enough funds")
        return

    new_balance = await db.change_balance(user_id, -amount)

    await callback.message.answer(
        f"Withdrawn {amount}$\n New balance: {new_balance}$"
    )