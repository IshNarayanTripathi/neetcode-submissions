class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapi = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in mapi:
                return [mapi[complement], i]
            mapi[num] = i