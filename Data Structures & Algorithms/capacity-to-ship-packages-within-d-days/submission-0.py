class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        min_weight = float("inf")
        while left <= right:
            mid = left+(right-left)//2
            temp = mid
            curr_days = 0
            i = 0
            while i < len(weights):
                while i < len(weights) and mid-weights[i] >=0:
                    mid -= weights[i]
                    i+=1
                curr_days += 1
                mid = temp
            if curr_days <= days:
                min_weight = min(min_weight, temp)
                right = mid-1
            else:
                left = mid+1
        return min_weight
                

