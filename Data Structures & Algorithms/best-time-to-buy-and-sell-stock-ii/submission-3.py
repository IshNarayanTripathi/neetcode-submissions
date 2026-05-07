class Solution:
    def maxProfit(self, price: List[int]) -> int:
        total = 0
        buying = price[0]
        for i in range(1, len(price)):
            if price[i] <= buying:
                buying = price[i]
            else:
                total += price[i]-buying
                buying = price[i]
        return total

        