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
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> out;
        function<void(TreeNode*)> dfs = [&](TreeNode* root) {
            if (!root || out.size() >= k) {
                return;
            }

            dfs(root->left);
            out.push_back(root->val);
            dfs(root->right);
        };
        dfs(root);
        return out[k - 1];
    }
};
