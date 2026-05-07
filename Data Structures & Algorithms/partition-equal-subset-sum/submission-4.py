class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        block = [0]*2
        def dfs(i):
            if i >=  len(nums):
                return all(b == target for b in block)
            for j in range(2):
                if block[j] + nums[i] <= target:
                    block[j] += nums[i]
                    if dfs(i+1):
                        return True
                    block[j] -= nums[i]
                if not block[j]:
                    break
            return False
        return dfs(0)