class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool word = false;
};

class WordDictionary {
private:
    TrieNode* root = new TrieNode();

    bool dfs(TrieNode* node, string word) {
        if (word.empty()) return node->word;

        char char_to_check = word[0];
        string rest_of_word = word.substr(1);

        if (char_to_check == '.') {
            for (pair<const char, TrieNode*> child : node->children) {
                if (dfs(child.second, rest_of_word)) return true;
            }
            return false;
        } 
        
        if(node->children.contains(char_to_check)) {
            return dfs(node->children[char_to_check], rest_of_word);
        }

        return false;
    }

public:
    void addWord(string word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (!curr->children.contains(c)) curr->children[c] = new TrieNode();
            curr = curr->children[c];
        }
        curr->word = true;
    }
    
    bool search(string word) {
        return dfs(root, word);
    }
};
