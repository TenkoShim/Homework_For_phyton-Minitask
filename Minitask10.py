from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value

    def get(self, key):
        if key not in self.cache:
            return None
        value = self.cache[key]
        del self.cache[key]
        self.cache[key] = value
        return value
c=LRUCache()

for i in range(18):
    c.put(i, i**2)
value=c.get("A")
print(value)
print(vars(c))