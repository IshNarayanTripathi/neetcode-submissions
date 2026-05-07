class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = nums[0]
        for i in nums:
            if majority == i:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority = i
                    count = 1
        return majority