class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []
        curr = []

        def is_palindrome(s, i, j) -> bool:
            l, r = i, j
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if i == len(s):
                out.append(curr.copy())
                return
            
            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    curr.append(s[i:j + 1])
                    dfs(j + 1)
                    curr.pop()
        
        dfs(0)
        return out