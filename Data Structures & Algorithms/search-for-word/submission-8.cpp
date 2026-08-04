class Solution {
private:
    static constexpr char VISITED_MARKER = '#';

    bool dfs(auto& board, int r, int c, int i, const string& word) {
        if (i == word.size()) return true;
        if (r < 0 || r >= ssize(board) || c < 0 || c >= ssize(board[0])) return false;
        if (board[r][c] != word[i]) return false;

        char original_char = board[r][c];
        board[r][c] = VISITED_MARKER;

        bool word_found = dfs(board, r - 1, c, i + 1, word) || 
            dfs(board, r + 1, c, i + 1, word) || 
            dfs(board, r, c - 1, i + 1, word) ||
            dfs(board, r, c + 1, i + 1, word);
        
        board[r][c] = original_char;
        return word_found;
    }

public:
    bool exist(vector<vector<char>>& board, string word) {
        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[r].size(); c++) {
                if (board[r][c] == word[0] && dfs(board, r, c, 0, word)) return true;
            }
        }
        return false;
    }
};
