class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in hm:
                hm[key].append(word)
            else:
                hm[key] = [word]
        return list(hm.values())