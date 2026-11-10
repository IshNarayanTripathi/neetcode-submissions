class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = float("inf")
        while l <= r:
            mid = l + (r-l)//2
            curr_time = 0
            for pile in piles:
                curr_time += math.ceil(pile/mid)
                
            if curr_time > h:
                l = mid+1
                
            else:
                r = mid-1
                ans = min(ans, mid)
            
        return ans
        