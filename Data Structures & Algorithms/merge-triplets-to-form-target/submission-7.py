class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # for i in range(len(triplets)):
        #     if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
        #         return False
        if len(triplets) == 1:
            return triplets[0] == target
        i, j = 0, 1
        while i < len(triplets) and j < len(triplets):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                i += 1
                if i == j:
                    j += 1
            elif triplets[j][0] > target[0] or triplets[j][1] > target[1] or triplets[j][2] > target[2]:
                j += 1
            else:
                triplets[j][0] = max(triplets[i][0], triplets[j][0])
                triplets[j][1] = max(triplets[i][1], triplets[j][1])
                triplets[j][2] = max(triplets[i][2], triplets[j][2])
                if triplets[j] == target:
                    return True
                i += 1
                j += 1
        return False

   
