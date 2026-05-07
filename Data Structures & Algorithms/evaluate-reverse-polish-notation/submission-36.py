class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                val1 = nums.pop()
                val2 = nums.pop()
                if token == "+":
                    nums.append(val2 + val1)
                elif token == "-":
                    nums.append(val2 - val1)
                elif token == "*":
                    nums.append(val2 * val1)
                else:
                    nums.append(int(val2 / val1))
            else:
                nums.append(int(token))
        return nums[0]