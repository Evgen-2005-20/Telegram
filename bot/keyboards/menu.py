from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Balance", callback_data="balance")],
            [InlineKeyboardButton(text="Register", callback_data="Register")]
        ]
    )