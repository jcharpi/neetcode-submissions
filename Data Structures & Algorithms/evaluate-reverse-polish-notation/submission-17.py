class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        while i < len(tokens):
            stack.append(tokens[i])
            if ((len(tokens) > 2) and
             (stack[-1] == "+") or
             (stack[-1] == "-") or
             (stack[-1] == "*") or
             (stack[-1] == "/")):
             op = stack.pop()
             num1 = int(stack.pop())
             num2 = int(stack.pop())
             match op:
                case "+":
                    stack.append(num1 + num2)
                case "-":
                    stack.append(num2 - num1)
                case "*":
                    stack.append(num1 * num2)
                case "/":
                    stack.append(math.trunc(num2/num1))
            i += 1
        return int(stack[0])