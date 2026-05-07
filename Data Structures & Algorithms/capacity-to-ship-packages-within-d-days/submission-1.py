class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left, right = min(weights), sum(weights)
        min_weight = float("inf")
        while left <= right:
            mid = left + (right-left)//2
            count = 1
            curr_weight = 0
            for weight in weights:
                if weight > mid:
                    count = float("inf")
                    break
                curr_weight += weight
                if curr_weight > mid:
                    count += 1
                    curr_weight = weight
            if count <= days:
                min_weight = min(min_weight, mid)
                right = mid-1
            else:
                left = mid+1
        return min_weight