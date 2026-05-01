class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            out += f"{len(word)}${word}"
        return out 
    def decode(self, s: str) -> List[str]:
        i, out = 0, []

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            
            length = int(s[i:j])

            out.append(s[j+1:j+1+length])

            i = j+1+length

        return out