class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        curr_sqrt = float("-inf")
        while left <= right:
            mid = left+(right-left)//2
            if mid*mid <= x:
                curr_sqrt = max(curr_sqrt, mid)
                left = mid+1
            else:
                right  = mid-1
        return curr_sqrt