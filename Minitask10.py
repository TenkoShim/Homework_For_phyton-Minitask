from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity=16):
        self.__capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) >= self.__capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    @property
    def capacity(self):
        return self.__capacity


c = LRUCache(capacity=20)
print(c.capacity)
for i in range(c.capacity):
    c.put(i, i ** 2)
value = c.get("A")
print(value)
print(vars(c))
