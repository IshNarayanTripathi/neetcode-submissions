class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        partition = [0]*k
        nums.sort(reverse=True)
        target = total // k
        def backtrack(ind):
            if ind == len(nums):
                return all(b == target for b in partition)
            for i in range(k):
                if partition[i]+nums[ind] <= target:
                    partition[i] += nums[ind]
                    if backtrack(ind+1):
                        return True
                    partition[i] -= nums[ind]
                if not partition[i]:
                    break
            return False
        return backtrack(0)