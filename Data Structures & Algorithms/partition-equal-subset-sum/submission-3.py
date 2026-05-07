class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        bucket = [0]*2
        def dfs(i):
            if i == len(nums):
                return all(b == target for b in bucket)
            for j in range(2):
                if bucket[j] + nums[i] <= target:
                    bucket[j] += nums[i]
                    if dfs(i+1):
                        return True
                    bucket[j] -= nums[i]
                if not bucket[j]:
                    break
            return False
        return dfs(0)