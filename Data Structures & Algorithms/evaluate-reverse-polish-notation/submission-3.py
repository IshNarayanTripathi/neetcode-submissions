class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['+', '*', '-', '/']:
                stack.append(int(i))
            elif i == '+':
                second_val = stack.pop()
                first_val = stack.pop()
                stack.append(first_val+second_val)
            elif i == '-':
                second_val = stack.pop()
                first_val = stack.pop()
                stack.append(first_val-second_val)
            elif i == "*":
                second_val = stack.pop()
                first_val = stack.pop()
                stack.append(first_val*second_val)
            elif i == '/':
                second_val = stack.pop()
                first_val = stack.pop()
                stack.append(int(first_val/second_val))
        return stack[-1]