class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # left, right = 0, len(nums)-1
        # while left <= right:
        #     if nums[left] + nums[right] == target:
        #         return [left, right]
        #     elif nums[left] + nums[right] > target:
        #         right -= 1
        #     else:
        #         left += 1
        mapi = {}
        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in mapi:
                if i > mapi[complement]:
                    return [mapi[complement], i]
                else:
                    return [i, mapi[complement]]
            else:
                mapi[nums[i]] = i
        










