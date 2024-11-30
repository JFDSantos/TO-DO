import redis

REDIS_HOST = "todo_redis"
REDIS_PORT = 6379

def get_redis():
    return redis.StrictRedis(host="localhost", port=REDIS_PORT, db=0, decode_responses=True)

def store_token_in_cache(username: str, token: str, expiration: int = 3600):
    redis_client = get_redis()
    redis_client.set(f"token:{username}", token, ex=expiration)

def get_token_from_cache(username: str):
    redis_client = get_redis()
    return redis_client.get(f"token:{username}")



