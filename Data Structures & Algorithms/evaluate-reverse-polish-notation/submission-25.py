class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        out = []
        for i in range (len(tokens)):
            if tokens[i] == "+":
                out.append(int(out.pop()) + int(out.pop()))
            elif tokens[i] == "-":
                val1, val2 = int(out.pop()), int(out.pop())
                out.append(val2 - val1)
            elif tokens[i] == "*":
                out.append(int(out.pop()) * int(out.pop()))
            elif tokens[i] == "/":
                val1, val2 = int(out.pop()), int(out.pop())
                out.append(int(val2 / val1))
            else:
                out.append(tokens[i])
        return int(out[0])