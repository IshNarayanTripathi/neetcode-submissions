class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return float("inf")
            if remain in memo:
                return memo[remain]
            min_coins = float("inf")
            for num in coins:
                res = dfs(remain-num)
                if res != float("inf"):
                    min_coins = min(min_coins, 1+res)
            memo[remain] = min_coins
            return memo[remain]
        min_coins = dfs(amount)
        return min_coins if min_coins != float("inf") else -1