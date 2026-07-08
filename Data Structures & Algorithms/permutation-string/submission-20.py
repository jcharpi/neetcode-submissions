class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])

        if window == s1_count:
            return True

        for r in range(len(s1), len(s2)):
            window[s2[r]] += 1
            window[s2[r - len(s1)]] -= 1
            if window[s2[r - len(s1)]] == 0:
                del window[s2[r - len(s1)]]
            if window == s1_count:
                return True
            
        return False