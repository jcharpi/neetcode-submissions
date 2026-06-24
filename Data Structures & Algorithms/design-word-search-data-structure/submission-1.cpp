class TrieNode {
public:
    unordered_map<char, TrieNode*> children = {};
    bool word = false;
};

class WordDictionary {
    TrieNode* root = new TrieNode();
public:
    void addWord(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (!curr->children.count(c)) {
                curr->children[c] = new TrieNode();
            }
            curr = curr->children[c];
        }
        curr->word = true;
    }
    
    bool search(string word) {
        return dfs(root, word);
    }
private:
    bool dfs(TrieNode* node, string word) {
        if (word.empty()) {
            return node->word;
        }

        char c = word[0];
        string rest = word.substr(1);
        
        if (c == '.') {
            for (pair<const char, TrieNode*>& p : node->children) {
                if (dfs(p.second, rest)) {
                    return true;
                }
            }
            return false;
        } else if (!node->children.count(c)) {
            return false;
        }
        return dfs(node->children[c], rest);
    }
};
