class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # valid until we hit a character outside the range of permutations
        # then set l = r and restart

        # if we find that all chars of a permutation are next to each other return True
        l, r = 0, len(s1) - 1

        while r < len(s2):
            print(Counter(s1), Counter(s2[l:r+ 1]))
            if Counter(s1) == Counter(s2[l:r + 1]):
                return True
            l += 1
            r += 1
        return False