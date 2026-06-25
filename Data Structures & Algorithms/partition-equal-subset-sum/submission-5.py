class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        block = [0]*2
        def dfs(ind):
            if ind == len(nums):
                return all(b == target for b in block)
            for i in range(2):
                if block[i] + nums[ind] <= target:
                    block[i] += nums[ind]
                    if dfs(ind+1):
                        return True
                    block[i] -= nums[ind]
                if block[i] == 0:
                    break
                        
                    
            return False
        return dfs(0)