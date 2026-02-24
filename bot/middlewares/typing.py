import asyncio
from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.enums import ChatAction


class TypingMessage(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, Message):
            bot = data["bot"]

            await bot.send_chat_action(
                chat_id=event.chat.id,
                action=ChatAction.TYPING
            )

            await asyncio.sleep(2)

        return await handler(event, data)