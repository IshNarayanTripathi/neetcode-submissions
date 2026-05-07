class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        targetSum = 0
        for i in s1:
            targetSum += ord(i)
        for right in range(len(s1)-1, len(s2)):
            curr_sum = 0
            sum_left = left
            while sum_left <= right:
                curr_sum += ord(s2[sum_left])
                sum_left += 1
            if targetSum == curr_sum and sorted(s1) == sorted(s2[left:right+1]):

                return True
            left += 1
        return False