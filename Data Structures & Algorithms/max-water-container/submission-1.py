class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxa = float("-inf")
        left, right = 0, len(heights)-1
        while left < right:
            maxa = max(maxa, min(heights[left], heights[right])*
                (right-left))
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxa