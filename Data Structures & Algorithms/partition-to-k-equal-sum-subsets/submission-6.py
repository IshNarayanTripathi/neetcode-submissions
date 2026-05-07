class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        block = [0]*k
        def backtrack(ind):
            if ind == len(nums):
                return all(b == target for b in block)
            for i in range(k):
                if block[i]+nums[ind] <= target:
                    block[i] += nums[ind]
                    if backtrack(ind+1):
                        return True
                    block[i] -= nums[ind]
                if not block[i]:
                    break
            return False
        return backtrack(0)