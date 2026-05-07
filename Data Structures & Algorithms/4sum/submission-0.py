class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            first = nums[i]
            for j in range(i+1, len(nums)):
                second = nums[j]
                left = j+1
                right = len(nums)-1
                while left < right:
                    if first+second+nums[left]+nums[right]==target:
                        res.add((first,second,nums[left],nums[right]))
                        left+=1
                        right-=1
                    elif first+second+nums[left]+nums[right]>target:
                        right-=1
                    else:
                        left+=1
        return list(res)                        