class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        min_val = float("inf")
        if self.minStack:
            min_val = min(val, self.minStack[-1])
        self.stack.append(val)
        self.minStack.append(min_val if min_val != float("inf") else val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
