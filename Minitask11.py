from collections import OrderedDict
# class SingletonMeta(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]
#
# class SingletonClass(metaclass=SingletonMeta):
#     pass
#
# obj1 = SingletonClass()
# obj2 = SingletonClass()
# print(id(obj1) == id(obj2))
def singleton(clas):
    incopies={}
    def get_copy(*args,**kwargs):
        if clas not in incopies:
            incopies[clas]=clas(*args,*kwargs)
        return incopies[clas]
    return get_copy
@singleton
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
c1=LRUCache()
c2=LRUCache(20)
print(id(c1)==id(c2))
