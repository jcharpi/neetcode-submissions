class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += f"{len(word)}${word}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        print(s)
        # i = j; while not pointing at delimeter ($) advance j 
        ### we can do this because we know legnth will never have delimeter in it
        out, i = [], 0
        while i < len(s) - 1:
            j = i
            while s[j] != "$":
                j += 1
        # length = s[i:j]
            length = int(s[i:j])

        # word = s[i+j:i+j+length]
            word = s[j+1:j+1+length]
            out.append(word)
            i = j+1+length
            print(word)
        # probably a plus one in there somewhere 
        return out