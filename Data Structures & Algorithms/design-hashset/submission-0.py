class MyHashSet:

    def __init__(self):
        self.mapp = []

    def add(self, key: int) -> None:
        if key not in self.mapp:
            self.mapp.append(key)

    def remove(self, key: int) -> None:
        if key in self.mapp:
            self.mapp.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.mapp:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)