class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            mid = len(nums)//2
            left = self.sortArray(nums[:mid])
            right = self.sortArray(nums[mid:])
            k = m = n = 0
            while m < len(left) and n < len(right):
                if left[m] <= right[n]:
                    nums[k] = left[m]
                    m += 1
                else:
                    nums[k] = right[n]
                    n += 1
                k += 1
            while m < len(left):
                nums[k] = left[m]
                k += 1
                m += 1
            while n < len(right):
                nums[k] = right[n]
                k += 1
                n += 1
        return nums