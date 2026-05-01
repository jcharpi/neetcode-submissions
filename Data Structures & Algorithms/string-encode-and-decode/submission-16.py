class Solution:
    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            out += f"{len(word)}#{word}"
        return out

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # init array and starting point
        while i < len(s): # move through decoded string
            j = i # set two pointers
            while s[j] != "#": 
                j += 1
            length = int(s[i:j]) #length == starting point through j
            res.append(s[j+1:length+j+1]) #j+1 = the char after the '#':the end of the word
            i = length+j+1 #increment i to first length of new word
        return res
        # look at number while not #, increment
