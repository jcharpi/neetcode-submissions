class Solution {
private:
    void dfs(size_t i, const string& digits, const unordered_map<char, string>& digit_to_letters, string& curr, vector<string>& out) {
        if (i == digits.size()) {
            out.push_back(curr);
            return;
        }

        for (char letter : digit_to_letters.at(digits[i])) {
            curr.push_back(letter);
            dfs(i + 1, digits, digit_to_letters, curr, out);
            curr.pop_back();
        }
    }

public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        static const unordered_map<char, string> digit_to_letters = {
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, 
            {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, 
            {'8', "tuv"}, {'9', "wxyz"}
        };

        vector<string> out;
        string curr;
        curr.reserve(digits.size());
        
        dfs(0, digits, digit_to_letters, curr, out);
        return out;
    }
};
