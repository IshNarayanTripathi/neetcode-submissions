class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        window = len(count1)
        for i in range(len(s2)):
            count2, curr = defaultdict(int), 0
            for j in range(i, len(s2)):
                count2[s2[j]]+=1
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                elif count1.get(s2[j], 0) == count2[s2[j]]:
                    curr += 1
                if curr == window:
                    return True
        return False
