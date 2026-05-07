class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        left, right = 1, max(piles)
        min_cap = float("inf")
        while left <= right:
            mid = left + (right-left)//2
            hours = 0
            for i in piles:
                if i//mid == 0:
                    hours += 1
                else:
                    hours += i//mid
                    if i%mid:
                        hours += 1
            if hours <= h:
                min_cap = min(min_cap, mid)
                right = mid-1
            else:
                left = mid+1
        return min_cap