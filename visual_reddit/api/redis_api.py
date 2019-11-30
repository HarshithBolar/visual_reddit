import redis


class MyRedis:
    def __init__(self):
        self.db = redis.Redis(host='localhost', port=6379, db=0)  # , password="foobared"

    def store(self, key, value, timeout):
        return self.db.set(key, value, ex=timeout)

    def retrieve(self, key):
        return self.db.get(key)

    def fetch_images_from_cache(self, cached_images):
        cached_image_dict = {}
        for entry in cached_images:
            path, title = entry.split("|")
            submission_id = path.split("/")[-1]
            cached_image_dict[submission_id] = (path, title)
        return cached_image_dict
