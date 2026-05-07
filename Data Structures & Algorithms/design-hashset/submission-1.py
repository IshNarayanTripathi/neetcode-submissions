class MyHashSet:

    def __init__(self):
        self.cont = {}

    def add(self, key: int) -> None:
        if key not in self.cont:
            self.cont[key] = 1

    def remove(self, key: int) -> None:
        if key in self.cont:
            del self.cont[key]

    def contains(self, key: int) -> bool:
        if key in self.cont:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)