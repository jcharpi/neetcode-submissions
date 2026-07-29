class Solution {
private:
    void dfs(size_t i, vector<string>& letter_candidates, string& curr, vector<string>& out) {
        if (i == letter_candidates.size()) {
            out.push_back(curr);
            return;
        }

        const string& i_letters = letter_candidates.at(i);
        for (char c : i_letters) {
            curr.push_back(c);
            dfs(i + 1, letter_candidates, curr, out);
            curr.pop_back();
        }
    }

public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> out;
        string curr;

        const unordered_map<char, string> digit_to_letters = {
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, 
            {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, 
            {'8', "tuv"}, {'9', "wxyz"}
        };

        vector<string> letter_candidates;
        for (char c : digits) {
            letter_candidates.push_back(digit_to_letters.at(c));
        }

        dfs(0, letter_candidates, curr, out);
        return out;
    }
};
