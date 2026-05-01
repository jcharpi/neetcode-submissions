class Solution:
    def isPalindrome(self, s: str) -> bool:
        # place i at front, j at end
        i, j = 0, len(s) - 1

        def alphaNumeric(c):
            return ((ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')))

        while i < j:
            # while ascii code isn't a letter, move pointer forward or backward respectively
            while i < j and not alphaNumeric(s[i].lower()):
                i += 1
            while i < j and not alphaNumeric(s[j].lower()):
                j -= 1
            
            # compare pointers if both on letters; ignore case and advance each one.
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
            
        return True