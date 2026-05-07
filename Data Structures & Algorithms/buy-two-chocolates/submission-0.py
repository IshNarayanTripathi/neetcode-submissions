class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        res = float("-inf")
        prices.sort()
        left, right = 0, len(prices)-1
        while left < right:
            if prices[left] + prices[right] <= money:
                res = max(res, money - (prices[right]+prices[left]))
                # left += 1
                right -= 1
            else:
                right -= 1
        return res if res != float("-inf") else money
