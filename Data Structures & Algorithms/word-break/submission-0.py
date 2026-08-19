class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [False] * (len(s) + 1)
        cache[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                print(not cache[i], s[:i], i - len(word))
                if not cache[i] and s[:i].endswith(word) and cache[i - len(word)]:
                    cache[i] = True
        return cache[-1]