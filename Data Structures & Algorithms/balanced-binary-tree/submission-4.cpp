/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    pair<int, bool> dfs(TreeNode* root) {
        if (!root) return {0, true};

        pair<int, bool> left = dfs(root->left);
        pair<int, bool> right = dfs(root->right);
        bool isBalanced = left.second && right.second && abs(left.first - right.first) < 2;

        return {1 + max(left.first, right.first), isBalanced};
    }

public:
    bool isBalanced(TreeNode* root) {
        return dfs(root).second;
    }
};
