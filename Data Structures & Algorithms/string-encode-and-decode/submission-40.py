class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        i, out = 0, []
        
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            out.append(word)
            i = 1 + j + length
        
        return out
