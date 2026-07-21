class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        self.hashset.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.hashset)-1, -1, -1):
            if self.hashset[i] == key:
                self.hashset.pop(i)

    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)