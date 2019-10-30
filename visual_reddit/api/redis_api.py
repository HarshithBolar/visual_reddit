import redis

class MyRedis:
    def __init__(self):
        self.db = redis.Redis(host='localhost', port=6379, db=0, password="foobared")

    def store(self, key, value, timeout):
        return self.db.setex(key, timeout, value)

    def retrieve(self, key):
        return self.db.get(key)