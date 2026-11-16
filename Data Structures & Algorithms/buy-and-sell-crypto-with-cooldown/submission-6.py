class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def traverse(ind, buying):
            if ind >= n:
                return 0
            if (ind, buying) in dp:
                return dp[(ind, buying)]
            res = 0
            if buying:
                res += max(traverse(ind+1, False) -prices[ind], traverse(ind+1, True))
            if not buying:
                res += max(traverse(ind+2, True) +prices[ind], traverse(ind+1, False))
            dp[(ind, buying)] = res
            return dp[(ind, buying)]
        return traverse(0, True)