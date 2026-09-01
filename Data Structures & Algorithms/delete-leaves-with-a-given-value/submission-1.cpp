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
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        function<TreeNode*(TreeNode* node)> dfs = [&](TreeNode* node) -> TreeNode* {
            if (!node) return nullptr;

            node->left = dfs(node->left);
            node->right = dfs(node->right);

            if (node->val == target && !node->left && !node->right) return nullptr;

            return node;
        };

        return dfs(root);
    }
};