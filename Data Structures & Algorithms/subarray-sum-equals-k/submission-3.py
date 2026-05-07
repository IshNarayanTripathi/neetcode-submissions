class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        currSum = res = 0
        for num in nums:
            currSum +=  num
            res += prefixSum[currSum-k]
            prefixSum[currSum] += 1
        return res