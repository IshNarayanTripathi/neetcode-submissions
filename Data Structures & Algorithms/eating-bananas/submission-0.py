class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_k = float('inf')
        while left <= right:
            mid = left+(right-left)//2
            curr_time = 0
            for i in piles:
                curr_time += math.ceil(i/mid)
            if  curr_time <= h:
                min_k = min(min_k, mid)
                right = mid-1
            else:
                left = mid+1
        return min_k