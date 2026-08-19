class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [None] * (len(s) + 1)
        cache[0] = True

        def can_break(i):
            if cache[i] != None:
                return cache[i]
        
            cache[i] = False
            for word in wordDict:
                if s.endswith(word, 0, i) and can_break(i - len(word)):
                    cache[i] = True
                    break
            return cache[i]
        
        return can_break(len(s))
