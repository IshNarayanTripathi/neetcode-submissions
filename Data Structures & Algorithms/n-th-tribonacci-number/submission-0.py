class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        else:
            tribo = [0]*(n+1)
            tribo[0] = 0
            tribo[1] = 1
            tribo[2] = 1
            for i in range(3, n+1):
                tribo[i] = tribo[i-1]+tribo[i-2]+tribo[i-3]
            return tribo[n]