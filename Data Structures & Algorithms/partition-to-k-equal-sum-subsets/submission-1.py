class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        side = total // k
        sides = [0]*k
        nums.sort(reverse=True)
        def backtrack(ind):
            if ind == len(nums):
                return all(s == side for s in sides)
            for i in range(k):
                if sides[i]+nums[ind]<=side:
                    sides[i]+=nums[ind]
                    if backtrack(ind+1):
                        return True
                    sides[i]-=nums[ind]
                    if sides[i] == 0:
                        break
            return False
        return backtrack(0)
