class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # valid if openCount == closeCount == n
        # add open if openCount < n
        # add close if closeCount < openCount
        
        stack = []
        res = []

        def backtrack(closed_count, open_count):
            if closed_count == open_count == n:
                res.append("".join(stack))
                return
            
            if open_count < n:
                stack.append("(")
                backtrack(closed_count, open_count + 1)
                stack.pop()
            
            if closed_count < open_count:
                stack.append(")")
                backtrack(closed_count + 1, open_count)
                stack.pop()
        backtrack(0,0)
        return res