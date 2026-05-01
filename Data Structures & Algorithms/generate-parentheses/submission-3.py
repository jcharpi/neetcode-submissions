class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        stack = []
        # base case: open == closed == n
        # can add open until open == n
        # when closed < open: add closed
        def backtrack(opened, closed):
            if opened == closed == n:
                out.append("".join(stack))
                return
            
            if opened < n:
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()
            
            if closed < opened:
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()

        backtrack(0, 0)
        return out