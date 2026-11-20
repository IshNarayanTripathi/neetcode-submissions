class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        n = len(temperatures)
        stack = []
        for i in range(n-1, -1, -1):
            temp = temperatures[i]
            while stack and stack[-1][1] <= temp:
                stack.pop()
            if stack and stack[-1][1] > temp:
                ind, _ = stack[-1]
                res[i] = ind-i
            stack.append([i, temp])
        return res