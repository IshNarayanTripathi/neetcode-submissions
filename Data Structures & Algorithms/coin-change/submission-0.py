class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = float("inf")
            for num in coins:
                if amount-num >= 0:
                    res = min(res, 1+dfs(amount-num))
            memo[amount] = res
            return res
        mincoin = dfs(amount)
        return -1 if mincoin >= float("inf") else mincoin   
            
                