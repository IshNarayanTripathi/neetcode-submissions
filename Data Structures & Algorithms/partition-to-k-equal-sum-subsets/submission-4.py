class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k != 0:
            return False
        
        target = sum(nums)//k
        bucket = [0]*k
        def backtrack(ind):
           
            if ind == len(nums):
                return all(b == target for b in bucket)
            for j in range(k):
                if bucket[j]+nums[ind] <= target:
                    bucket[j] += nums[ind]
                    if backtrack(ind+1):
                        return True
                    bucket[j] -= nums[ind]
                if bucket[j] == 0:
                    break
            return False
        return backtrack(0)
            
