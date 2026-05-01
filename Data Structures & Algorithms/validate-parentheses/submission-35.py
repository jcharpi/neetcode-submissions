class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = { '}' : '{', ']' : '[', ')' : '(' }

        for bracket in s:
            if len(s) % 2 != 0:
                return False
            
            if bracket == '{' or bracket == '[' or bracket == '(':
                stack.append(bracket)
            elif stack and stack.pop() != brackets[bracket]:
                return False
        return len(stack) == 0 and s[0] not in brackets