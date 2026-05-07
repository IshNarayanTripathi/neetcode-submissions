class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(i)
            elif i == '+':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1+num2)
            elif i == '-':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1-num2)
            elif i == '*':
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1*num2)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                stack.append(num1/num2)
        return int(stack[0])