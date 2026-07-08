class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ("+", "-", "*", "/"):
                val1, val2 = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(val1 + val2) 
                elif token == "-":
                    stack.append(val2 - val1) 
                elif token == "*":
                    stack.append(val1 * val2) 
                else:
                    stack.append(int(val2 / val1))
            else:
                stack.append(int(token))
        return stack[0] if stack else []