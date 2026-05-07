class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr)>1:
            mid = len(arr)//2
            L = self.sortArray(arr[:mid])
            R = self.sortArray(arr[mid:])
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1
            while i < len(L):
                arr[k] = L[i]
                i+=1
                k+=1
            while j < len(R):
                arr[k] = R[j]
                j+=1
                k+=1
        return arr
            