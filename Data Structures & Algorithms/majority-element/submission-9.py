class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = nums[0], 1
        for num in nums[1:]:
            if num == major:
                count += 1
            if num != major:
                count -= 1
            if count == 0:
                major = num
                count = 1
        return major