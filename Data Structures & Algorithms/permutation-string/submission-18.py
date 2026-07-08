class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        l, window = 0, []

        for r in range(len(s2)):
            if len(window) < len(s1):
                window.append(s2[r])
                continue
            
            if Counter(window) == s1_counts:
                return True
            window = window[1:]
            window.append(s2[r])
            
            
        return True if Counter(window) == s1_counts else False