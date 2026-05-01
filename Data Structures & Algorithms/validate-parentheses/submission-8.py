class Solution:
    def isValid(self, s: str) -> bool:
        # ()[]
        # if char (, [, {, append to stack
        # else pop stack and compare 

        stack, i = [], 0
        key_map = {"[": "]", "{": "}", "(": ")"}

        if len(s) % 2 != 0:
            return False

        i = 0
        while i < len(s):
            if(s[i] == '(' or s[i] == '[' or s[i] == '{'):
                stack.append(s[i])
            else:
                if(not stack or key_map[stack.pop()] != s[i]):
                    return False
            i += 1
        return False if stack else True
