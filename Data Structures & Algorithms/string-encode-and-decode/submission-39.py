class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}${word}" for word in strs)
    
    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            j = s.index("$", i)
            length = int(s[i:j])
            word = s[j + 1:j + length + 1]
            out.append(word)
            i = j + length + 1
        return out
            
