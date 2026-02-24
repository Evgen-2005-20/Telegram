import asyncio
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ChatAction


class TypingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        bot = data["bot"]

        chat_id = None

        if isinstance(event, Message):
            chat_id = event.chat.id

        elif isinstance(event, CallbackQuery):
            chat_id = event.message.chat.id

        if chat_id:
            await bot.send_chat_action(
                chat_id=chat_id,
                action=ChatAction.TYPING
            )
            await asyncio.sleep(2)

        return await handler(event, data)