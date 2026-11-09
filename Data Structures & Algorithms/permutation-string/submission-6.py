from collections import  defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        target_sum = curr_sum = l = 0
        l1 = len(s1)
        count_s1 = defaultdict(int)
        count_s2 = defaultdict(int)
        for i in range(l1):
            target_sum += ord(s1[i])
            curr_sum += ord(s2[i])
            count_s1[s1[i]] += 1
            count_s2[s2[i]] += 1
        if target_sum == curr_sum:
            if count_s1 == count_s2:
                return True
        for r in range(l1, len(s2)):
            curr_sum += ord(s2[r]) - ord(s2[l])
            count_s2[s2[l]] -= 1
            if count_s2[s2[l]] == 0:
                del count_s2[s2[l]]
            count_s2[s2[r]] += 1
            if target_sum == curr_sum:
                if count_s1 == count_s2:
                    return True
            l += 1
        return False