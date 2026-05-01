class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(self.alphaNum(s[-1]))
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    def alphaNum(self, val: str) -> bool:
        if ((ord('0') <= ord(val) <= ord('9')) or 
        (ord('A') <= ord(val) <= ord('Z')) or 
        (ord('a') <= ord(val) <= ord('z'))):
            return True
        return False