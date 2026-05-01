class Solution:
    def isValid(self, s: str) -> bool:
        symbol_map = {"]" : "[", "}" : "{", ")" : "("}
        syms = []

        if len(s) % 2 != 0 or len(s) < 2:
            return False

        for i in range(len(s)):
            if ((s[i] == "{") or
                (s[i] == "[") or
                (s[i] == "(")):
                syms.append(s[i])
            elif (not syms or syms.pop() != symbol_map[s[i]]):
                return False
        return True if not syms else False
