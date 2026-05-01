class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for word in strs:
            out += f"{len(word)}${word}"
        print(out)
        return out

    def decode(self, s: str) -> List[str]:
        out, i = [], 0
        
        while i < len(s) - 1:
            j = i
            while s[j] != "$":
                j += 1
            
            length = int(s[i:j])
            out.append(s[j + 1:1 + j + length])
            i = j + 1 + length
        return out