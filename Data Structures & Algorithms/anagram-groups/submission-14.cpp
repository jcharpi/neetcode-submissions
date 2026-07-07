class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hm;
        for (const string &word : strs) {
            array<int, 26> counts{};
            for (char c : word) counts[c - 'a']++;

            string key;
            for (int count : counts) key += to_string(count) + "#";
            hm[key].push_back(word);
        }
        vector<vector<string>> out;
        for (pair<const string, vector<string>> &entry : hm) { 
            out.push_back(entry.second);
        }
        return out;
    }
};
