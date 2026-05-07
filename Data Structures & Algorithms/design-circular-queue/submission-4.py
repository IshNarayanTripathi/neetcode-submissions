class Node:
    def __init__(self, val=0, next=None):
        self.val =val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        self.size += 1
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
            return True
        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head
        return True

    def deQueue(self) -> bool:
        if not self.size:
            return False
        self.size -= 1
        if self.size == 0:
            self.head = self.tail = None
            return True
        self.head = self.head.next
        self.tail.next = self.head
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return not self.size

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()