class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k = float("inf")
        while left <= right:
            mid = left+(right-left)//2
            curr = 0
            for i in piles:
                curr += math.ceil(i/mid)
            if curr <= h:
                k = min(k, mid)
                right = mid-1
            else:
                left = mid+1
        return k
            