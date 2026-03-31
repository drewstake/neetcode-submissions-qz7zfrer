class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.od = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        # mark as most recently used
        self.od.move_to_end(key)
        return self.od[key]


    def put(self, key: int, value: int) -> None:
        if key in self.od:
            # update and mark as most recent
            self.od[key] = value
            self.od.move_to_end(key)
            return
        self.od[key] = value

        if len(self.od) > self.cap:
            self.od.popitem(last=False)
