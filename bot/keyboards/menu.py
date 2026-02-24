from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Balance", callback_data="balance")],
            [InlineKeyboardButton(text="Register", callback_data="register")]
        ]
    )
    

def balance_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="➕ Deposit 100", callback_data="deposit_100"),
                InlineKeyboardButton(text="➖ Withdraw 50", callback_data="withdraw_50"),
            ]
        ]
    )
