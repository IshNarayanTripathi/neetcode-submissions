from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            mapp[key].append(i)
        return [values for values in mapp.values()]