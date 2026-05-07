class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapi = {}
        for num in nums:
            if num in mapi:
                return True
            mapi[num] = True
        return False