class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        cand1 = cand2 = None
        count1 = count2 = 0
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        if nums.count(cand1) > n//3:
            res.append(cand1)
        if nums.count(cand2) > n//3:
            res.append(cand2)
        return res
                
            