class Solution:
    def isValid(self, s: str) -> bool:
        hm = { ')' : '(', '}' : '{', ']' : '[' }
        stack = []
        for c in s:
            # case 1: closing p
            if c in hm:
                # case 1: has opening partner
                if stack and stack[-1] == hm[c]:
                    stack.pop()
                # case 2: doesn't have opening partner
                else:
                    return False
            # case 2: opening p
            else:
                stack.append(c)
        return True if not stack else False