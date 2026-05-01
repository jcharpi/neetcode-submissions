class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {} # sorted: [words]
        for s in strs:
            sorted_s = sorted(s)
            joined_sorted_s = "".join(sorted_s)

            if joined_sorted_s in hm:
                hm[joined_sorted_s].append(s)
            else:
                hm[joined_sorted_s] = [s]
        return list(hm.values())
        