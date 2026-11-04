class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0]*n
        if s[0] != "0":
            dp[0] = 1
        for i in range(1, n):
            take1 = take2 = 0
            if s[i] != "0":
                take1 = dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                if i == 1:
                    take2 = 1
                else:
                    take2 = dp[i-2]
            dp[i] = take1 + take2
        return dp[n-1]
