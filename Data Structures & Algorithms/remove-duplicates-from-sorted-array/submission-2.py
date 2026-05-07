class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = set()
        res = []
        for num in nums:
            if num in visited:
                continue
            visited.add(num)
            res.append(num)
        nums[:] = res
        return len(nums)
