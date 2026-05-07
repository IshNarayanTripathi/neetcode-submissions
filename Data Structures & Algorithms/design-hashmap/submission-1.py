class MyHashMap:

    def __init__(self):
        self.cont = [-1]*2000
        self.divi = 2000

    def _hash(self, key):
        return key%self.divi

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        self.cont[index] = value

    def get(self, key: int) -> int:
        index = self._hash(key)
        return self.cont[index]

    def remove(self, key: int) -> None:
        index = self._hash(key)
        self.cont[index] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)