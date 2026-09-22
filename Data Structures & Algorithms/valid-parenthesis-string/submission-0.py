# Problem
# You are given a string s which contains only three types of characters: '(', ')' and '*'

# A string is valid if it follows all of the following rules:
# 1. Every left parenthesis '(' must have a corresponding right parenthesis ')' and vis versa
# 2. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# 3. A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".

# Goal:
# Return true if s is valid, otherwise return false.

# Solution
# - Length does not matter due to *
# - The sum of the minority parentheses count + * count need to be >= opening count

# - what if we keep count?
# -- bad because we can't know that all the elements are going to present themselves in a (*) ordering.
# -- as we encounter *, range of '(' becomes count of ( : count of ( + * count
# --- if we have come across a ), decrement our ( range by 1.
# --- if * count >= ( by the end, then we have enough
class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = max_open = 0
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:
                min_open -= 1
                max_open += 1
            
            min_open = max(min_open, 0)
            if max_open < 0:
                return False
        return min_open == 0

            