class Solution:
    def isValid(self, s: str) -> bool:
        symbol_map = {"]" : "[", "}" : "{", ")" : "("}
        stack = []

        if len(s) % 2 != 0 or len(s) < 2:
            return False

        for bracket in s:
            if ((bracket == "{") or
                (bracket == "[") or
                (bracket == "(")):
                stack.append(bracket)
            elif (not stack or stack.pop() != symbol_map[bracket]):
                return False
        return True if not stack else False
