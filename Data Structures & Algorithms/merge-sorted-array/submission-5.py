class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp1 = nums1[:m]
        l1, l2, k = 0, 0, 0
        while l1 < m and l2 < n:
            if temp1[l1] <= nums2[l2]:
                nums1[k] = temp1[l1]
                l1 += 1
            else:
                nums1[k] = nums2[l2]
                l2 += 1
            k += 1
        while l1 < m:
            nums1[k] = temp1[l1]
            k += 1
            l1 += 1
        while l2 < n:
            nums1[k] = nums2[l2]
            k += 1
            l2 += 1

        