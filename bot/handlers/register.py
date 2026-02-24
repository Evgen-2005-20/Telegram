from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from bot.states.states import Registration
from bot.db.db import rd
from bot.db.logic_db import RedisDataBase

router = Router()
database = RedisDataBase(redis_client=rd)


@router.callback_query(F.data == "register")
async def start_registration(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    user = await database.get_user(callback.from_user.id)
    if user:
        await callback.message.answer("You are already registered.")
        return

    await callback.message.answer("Enter your email:")
    await state.set_state(Registration.email)


@router.message(Registration.email)
async def get_email(message: Message, state: FSMContext):
    email = message.text

    if "@" not in email:
        await message.answer("Invalid email. Try again.")
        return

    await state.update_data(email=email)

    await message.answer("Enter your phone number:")
    await state.set_state(Registration.number)


@router.message(Registration.number)
async def get_number(message: Message, state: FSMContext):
    number = message.text

    if not number.isdigit() or len(number) < 10:
        await message.answer("Invalid phone number. Try again.")
        return

    await state.update_data(number=number)

    data = await state.get_data()

    result = await database.create_user(
        username=message.from_user.first_name,
        user_id=message.from_user.id,
        email=data["email"],
    )

    if result:
        await message.answer("Registration completed")
    else:
        await message.answer("Registration failed")

    await state.clear()