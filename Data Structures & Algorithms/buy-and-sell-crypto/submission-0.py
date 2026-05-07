class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buying = prices[0]
        for num in prices:
            curr = num - buying
            max_profit = max(max_profit, curr)
            buying = min(num, buying)
        return max_profit