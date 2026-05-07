class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        min_weight = float("inf")
        while left <= right:
            mid = left+(right-left)//2
            d =1
            curr = 0
            i = 0
            while i < len(weights):
                if curr+weights[i] > mid:
                    curr = weights[i]
                    d += 1
                    i += 1
                else:
                    curr += weights[i]
                    i+=1
            if d <= days:
                min_weight = min(min_weight, mid)
                right = mid-1
            else:
                left = mid+1
        return min_weight