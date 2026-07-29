class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digits_to_letters = {
            "2" : "abc", "3" : "def", "4" : "ghi", 
            "5" : "jkl", "6" : "mno", "7" : "pqrs",
            "8" : "tuv", "9" : "wxyz"
        }

        letter_candidates = []
        for digit in digits:
            letter_candidates.append(digits_to_letters[digit])

        out = []
        curr = []

        def dfs(i):
            if i == len(digits):
                out.append("".join(curr))
                return
            
            ith_letters = letter_candidates[i]
            for letter in ith_letters:
                curr.append(letter)
                dfs(i + 1)
                curr.pop()
        
        dfs(0)
        return out