class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:

        if key in self.cache:
            print(("Getting",(key, self.cache[key])))
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        print(("Putting", (key, value)))
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.cap:
            print(self.cache.popitem(last=False))
        
        
        
        
