class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        stack = []

        def backtrack (open_count, closed_count):
            if open_count == closed_count == n:
                out.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, closed_count)
                stack.pop()
            
            if closed_count < open_count:
                stack.append(")")
                backtrack(open_count, closed_count + 1)
                stack.pop()

        backtrack(0,0)
        return out