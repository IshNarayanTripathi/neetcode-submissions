class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = sum([int(i)**2 for i in str(n)])
            if n == 1:
                return True
        return False