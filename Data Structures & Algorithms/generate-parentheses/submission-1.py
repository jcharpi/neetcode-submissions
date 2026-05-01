class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # valid if openC == closeC == n
        # if openC < n add (
        # if closeC < openC add )

        stack = []
        res = []

        def backtrack(openC: int, closeC: int):
            if openC == closeC == n:
                res.append("".join(stack))
                return
            
            if openC < n:
                stack.append("(")
                backtrack(openC + 1, closeC)
                stack.pop()
            
            if closeC < openC:
                stack.append(")")
                backtrack(openC, closeC + 1)
                stack.pop()

        backtrack(0,0)
        return res