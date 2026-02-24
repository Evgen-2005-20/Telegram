from redis.asyncio import Redis

from bot.config import settings

rd = Redis(
    host=settings.HOST,
    port=settings.PORT,
    decode_responses=True
)