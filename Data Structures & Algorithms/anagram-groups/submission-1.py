class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. For each word in strs: splice str to array
        # 2. sort that array and check dict for it; else add it
        # 3. For each key in dict return values
        # sortedWord: [words]
        out = {}
        for word in strs:
            sortedWord = ''.join(sorted(list(word)))
            if(sortedWord in out):
                out[sortedWord].append(word)
            else:
                out[sortedWord] = [word]
        return list(out.values())