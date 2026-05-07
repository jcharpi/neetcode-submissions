class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            print(nums)
            if token == "*" or token == "/" or token == "+" or token == "-":
                val1 = int(nums.pop())
                val2 = int(nums.pop())
            else:
                nums.append(token)

            if token == "*":
                nums.append(val1 * val2)
            elif token == "/":
                nums.append(val2 / val1)
            elif token == "+":
                nums.append(val1 + val2)
            elif token == "-":
                nums.append(val2 - val1)
        return int(nums[-1])