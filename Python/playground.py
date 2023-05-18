import abc
from collections.abc import Sized

class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    x = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get(self, key):
        pass

    def set(self, key, value):
        pass

redis_cache = RedisCache(2, 3)
print(redis_cache.x)
print(RedisCache.x)