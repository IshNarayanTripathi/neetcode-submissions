class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        order = 0
        for num in nums:
            if num in s:
                continue
            nums[order] = num
            s.add(num)
            order += 1
        return order