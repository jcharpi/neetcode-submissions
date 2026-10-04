class Solution:
    def decodeString(self, s: str) -> str:
        string_stack, repeat_stack = [], []
        curr_string, pending_repeat = "", 0
        for char in s:
            if char.isdigit():
                 # go digit by digit (mult by 10 to move digit)
                pending_repeat = pending_repeat * 10 + int(char)
            elif char == '[':
                string_stack.append(curr_string)
                repeat_stack.append(pending_repeat)
                curr_string, pending_repeat = "", 0
            elif char == ']':
                outer_string, curr_repeat = string_stack.pop(), repeat_stack.pop()
                curr_string = outer_string + curr_string * curr_repeat
            else:
                curr_string += char
        return curr_string