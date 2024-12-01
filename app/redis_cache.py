import redis
import os
from urllib.parse import urlparse

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

parsed_redis_url = urlparse(REDIS_URL)
REDIS_HOST = parsed_redis_url.hostname or "localhost"
REDIS_PORT = parsed_redis_url.port or 6379

def get_redis():
    return redis.StrictRedis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        db=0,
        password=os.getenv("REDIS_PASSWORD"),
        decode_responses=True,
        ssl=True  # Habilita SSL para a comunicação segura
    )

def store_token_in_cache(username: str, token: str, expiration: int = 3600):
    redis_client = get_redis()
    redis_client.set(f"token:{username}", token, ex=expiration)

async def get_token_from_cache(username: str):
    redis_client = get_redis()
    return redis_client.get(f"token:{username}")
