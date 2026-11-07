class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        block = [0]*2
        n = len(nums)
        def check(ind):
            if ind == n:
                return all(b == target for b in block)
            for i in range(2):
                if block[i]+nums[ind] <= target:
                    block[i] += nums[ind]
                    if check(ind+1):
                        return True
                    block[i] -= nums[ind]
                if not block[i]:
                    break
            return False
        return check(0)

