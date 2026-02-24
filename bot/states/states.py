from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    email = State()
    number = State()