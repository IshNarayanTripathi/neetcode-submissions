class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i not in ["+","D","C"]:
                stack.append(int(i))
            elif i == "+":
                stack.append(stack[-1]+stack[-2])
            elif i == "D":
                stack.append(2*stack[-1])
            else:
                stack.pop()
        return sum(stack)