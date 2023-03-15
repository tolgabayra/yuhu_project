from flask_caching import Cache
from config import Config

cache = Cache(config={
    "CACHE_TYPE": Config.CACHE_TYPE,
    "CACHE_REDIS_URL": Config.CACHE_REDIS_URL
})

# Utils.py oluşturup ordan import edilmelidir.
