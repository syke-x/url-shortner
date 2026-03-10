import time 
from app.extensions.redis_client import redis_client

def is_rate_limited(key , limit , window):

    current_count = redis_client.incr(key)

    if current_count == 1:
        redis_client.expire(key , window)

    if current_count > limit:
        ttl = redis_client.ttl(key)
        return True , ttl
    
    return False , redis_client.ttl(key)