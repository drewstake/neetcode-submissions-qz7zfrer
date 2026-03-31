class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.hashMap.move_to_end(key)
            return self.hashMap[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap.move_to_end(key)
        self.hashMap[key] = value
        
        if len(self.hashMap) > self.capacity:
            self.hashMap.popitem(last=False)
        
