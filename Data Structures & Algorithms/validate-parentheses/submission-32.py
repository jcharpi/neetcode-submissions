class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { '}' : '{', ')' : '(', ']' : '['}
        stack = []

        if len(s) % 2 == 1:
            return False

        for char in s:
            if char == '{' or char == '(' or char == '[':
                stack.append(char)
            elif stack and stack.pop() != brackets[char]:
                return False
        return s[0] not in brackets and len(stack) == 0