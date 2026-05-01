class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1, 2, +
        # 3, 3, *
        # 9, 4 -
        stack = []

        i = 0
        while i < len(tokens):
            if(len(tokens) == 1):
                return int(tokens[0])
            stack.append(tokens[i])

            if stack[-1] == "+" or  stack[-1] == "/" or stack[-1] == "*" or stack[-1] == "-":
                op = stack.pop()
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                print(f"op: {op}, num1: {num1}, num2: {num2}")
                match op:
                    case "+":
                        result = num1+num2
                    case "-":
                        result = num2-num1
                    case "*":
                        result = num1*num2
                    case "/":
                        result = math.trunc(num2/num1)
                stack.append(result)
                print(result)
            i += 1
        return stack[0]

# 3+9 = 12
# 12 * -11 = -132
# 6 / -132 = 0
# 0 * 10 = 0
# 0 + 17 = 17