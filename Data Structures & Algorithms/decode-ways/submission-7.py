class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        n = len(s)
        def memo(ind):
            if ind >= n:
                return 1
            if s[ind] == "0":
                return 0
            if ind in dp:
                return dp[ind]
            
            res = memo(ind+1)
            
            if ind+1 < n and 10 <= int(s[ind: ind+2]) <= 26:
                res += memo(ind+2)
                
            dp[ind] = res
            return dp[ind]
        return memo(0)

            

