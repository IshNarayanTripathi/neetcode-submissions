class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heapq.heapify(nums)
        max_consecutive = 1
        curr_consecutive = 0
        prev_val = None
        while nums:
            val = heapq.heappop(nums)
            if prev_val is None:
                prev_val = val
                curr_consecutive += 1
                continue
            if prev_val == val:
                continue
            if prev_val == val-1:
                curr_consecutive += 1
                prev_val = val
                max_consecutive = max(max_consecutive, curr_consecutive)
            else:
                prev_val = val
                max_consecutive = max(max_consecutive, curr_consecutive)
                curr_consecutive = 1
        return max_consecutive


