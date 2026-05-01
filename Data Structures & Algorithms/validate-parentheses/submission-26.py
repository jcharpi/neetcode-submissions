class Solution:
    def isValid(self, s: str) -> bool:
        values = {")":"(", "}":"{", "]":"["}
        stack = []

        if len(s)%2 != 0:
            return False
        
        for i in range(len(s)):
            if (stack and( s[i] == ")" or s[i] == "]" or s[i] == "}")):
                if stack.pop() != values[s[i]]:
                    return False
            else:
                stack.append(s[i])
        print(stack)
        return True if len(stack) == 0 else False