import redis

from bot.config import settings

rd = redis.Redis(
    host=settings.HOST,
    port=settings.PORT,
    decode_responses=True
)