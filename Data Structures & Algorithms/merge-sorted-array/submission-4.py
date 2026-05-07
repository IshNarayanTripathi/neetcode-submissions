class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = nums1[:m]
        k = n1 = n2 = 0
        while n1 < m and n2 < n:
            if arr[n1] <= nums2[n2]:
                nums1[k] = arr[n1]
                n1 += 1
            else:
                nums1[k] = nums2[n2]
                n2 += 1
            k += 1
        while n1 < m:
            nums1[k] = arr[n1]
            n1 += 1
            k += 1
        while n2 < n:
            nums1[k] = nums2[n2]
            n2 += 1
            k += 1
        