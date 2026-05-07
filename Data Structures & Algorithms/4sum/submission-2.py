class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for  i  in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num1 = nums[i]

            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                num2 = nums[j]
                left = j+1
                right = len(nums)-1
                while left < right:
                    if num1+num2+nums[left]+nums[right]==target:
                        res.append([num1,num2,nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left +=  1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif num1+num2+nums[left]+nums[right]>target:
                        right -= 1
                    else:
                        left += 1
        return res
