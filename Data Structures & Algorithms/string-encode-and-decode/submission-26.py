class Solution:

    def encode(self, strs: List[str]) -> str:
        #cat, frog => cat#frog
        #c#at, frog => c, at, frog
        #4c#at, 4frog
        #1212341411#asl;dkjf;alsdkjfa;sldkfj
        out = ""
        for word in strs:
            out += f"{len(word)}#{word}"
        return out

    def decode(self, s: str) -> List[str]:
        out, i = [], 0
        print(s)
        while i < len(s) - 1:
            j = i
            #check for length
            while s[j] != '#':
                j += 1
            
            # 4#c#at4#frog
            print(f"i == {i}, j == {j}")
            length = int(s[i:j])
            print(f"length == {length}")
            word = s[j+1:j+1+length]
            out.append(word)
            
            i = j + 1 + length
        return out
