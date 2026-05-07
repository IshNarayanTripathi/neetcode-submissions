class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > curr_price:
                profit += prices[i] - curr_price
            curr_price = prices[i]
        return profit