class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #left = 0
        pointer = 0
        visited = set()
        for right in range(len(nums)):
            if pointer <= k:
                if nums[right] in visited:
                    return True
                visited.add(nums[right])
                pointer += 1
            else:
                pointer = 1
                visited = set()
                visited.add(nums[right])
        return False