class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}#{word}"
        return res

    def decode(self, s: str) -> List[str]:
        out, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            out.append(s[j+1:j+1+length])
            i = j + 1 + length
        return out
