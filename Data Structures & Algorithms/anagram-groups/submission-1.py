class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mapp = defaultdict(bool)
        for word in strs:
            mapp[word] = False
        for i, word in enumerate(strs):
            if not mapp[word]:
                curr_list = [word]
                mapp[word] = True
                for j in range(i+1, len(strs)):
                    if sorted(word) == sorted(strs[j]):
                        curr_list.append(strs[j])
                        mapp[strs[j]] = True
                res.append(curr_list)
        return res
            