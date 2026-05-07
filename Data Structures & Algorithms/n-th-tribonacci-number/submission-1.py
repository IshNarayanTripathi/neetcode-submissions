class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 3:
            return 2
        elif 0 < n < 3:
            return 1
        elif n == 0:
            return 0
        else:
            tri = [0]*(n+1)
            tri[1], tri[2] = 1, 1
            for i in range(3, n+1):
                tri[i] = tri[i-3]+tri[i-2]+tri[i-1]
            return tri[n]