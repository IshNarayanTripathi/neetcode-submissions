class Node:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.front = None
        self.rear = None

    def enQueue(self, val: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        new_node = Node(val)
        if self.front == None:
            self.front = self.rear = new_node
            new_node.next = new_node
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        return True

    def Front(self) -> int:
        if self.front:
            return self.front.val
        return -1

    def Rear(self) -> int:
        if self.rear:
            return self.rear.val
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

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