class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through strings
        # sortedString: [words]
        # return hm values

        hm = {}
        
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in hm:
                hm[sortedWord].append(word)
            else:
                hm[sortedWord] = [word]

        return list(hm.values())