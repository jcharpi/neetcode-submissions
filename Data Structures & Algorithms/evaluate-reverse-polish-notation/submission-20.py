class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i] == "+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif tokens[i] == "-":
                val1, val2 = int(stack.pop()), int(stack.pop())
                stack.append(val2 - val1)
            elif tokens[i] == "*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif tokens[i] == "/":
                val1, val2 = int(stack.pop()), int(stack.pop())
                stack.append(int(val2/val1))
            else:
                stack.append(tokens[i])
        return int(stack[0])