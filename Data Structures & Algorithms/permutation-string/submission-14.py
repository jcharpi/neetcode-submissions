class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
       
        l, r = 0, len(s1) - 1
        s1_counts = Counter(s1)
        s2_counts = Counter(s2[:r + 1])

        while r < len(s2):
            if s1_counts == s2_counts:
                return True

            s2_counts[s2[l]] -= 1
            if s2_counts[s2[l]] == 0:
                del s2_counts[s2[l]]
            l += 1
            r += 1
            if r < len(s2):
                s2_counts[s2[r]] = s2_counts.get(s2[r], 0) + 1

        return False