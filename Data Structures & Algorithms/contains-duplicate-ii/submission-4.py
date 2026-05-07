class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapi = {}
        for i, num in enumerate(nums):
            if num in mapi:
                if abs(i-mapi[num]) <= k:
                    return True
            mapi[num] = i
        return False