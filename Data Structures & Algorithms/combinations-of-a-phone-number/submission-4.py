class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            "2" : "abc", "3" : "def", "4" : "ghi", 
            "5" : "jkl", "6" : "mno", "7" : "pqrs",
            "8" : "tuv", "9" : "wxyz"
        }

        out, curr = [], []

        def dfs(i):
            if i == len(digits):
                out.append("".join(curr))
                return
            
            for letter in digit_to_letters[digits[i]]:
                curr.append(letter)
                dfs(i + 1)
                curr.pop()
        
        dfs(0)
        return out