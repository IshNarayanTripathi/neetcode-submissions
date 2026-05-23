class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapi = defaultdict(list)
        strs.sort()
        for num in strs:
            key = ''.join(sorted(num))
            mapi[key].append(num)
        return [val for val in mapi.values()]