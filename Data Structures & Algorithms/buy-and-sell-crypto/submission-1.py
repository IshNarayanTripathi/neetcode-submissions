class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = float("-inf")
        buying = prices[0]
        for num in prices[1:]:
            maxi = max(maxi, num-buying)
            if num < buying:
                buying = num
        return maxi if maxi > 0 else 0
