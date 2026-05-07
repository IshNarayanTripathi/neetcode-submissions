class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = set()
        def dfs(i):
            if i >= len(nums)-1:
                return True
            if i in visited:
                return False
            visited.add(i)
            for jump in range(1, nums[i]+1):
                if dfs(i+jump):
                    return True
            return False
            
        return dfs(0)