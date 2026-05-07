class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = float("-inf")
        left, right = 0, len(heights)-1
        while left < right:
            curr_area = min(heights[left], heights[right])*(right-left)
            area = max(area, curr_area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return area