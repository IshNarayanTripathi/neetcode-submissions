class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_val = float("inf")
        while left <= right:
            mid = left+(right-left)//2
            curr_sum = 0
            for pile in piles:
                curr_sum += math.ceil(pile/mid)
            if curr_sum <= h:
                min_val = min(min_val, mid)
                right = mid-1
            else:
                left = mid+1
        return min_val