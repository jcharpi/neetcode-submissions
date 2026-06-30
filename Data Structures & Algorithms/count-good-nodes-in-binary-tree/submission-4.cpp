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
    int goodNodes(TreeNode* root) {
        function<int(TreeNode*, int)> dfs = [&](TreeNode* root, int maxSeen) -> int {
            if (!root) return 0;

            int count = root->val >= maxSeen ? 1 : 0;
            maxSeen = max(maxSeen, root->val);

            return count + dfs(root->left, maxSeen) + dfs(root->right, maxSeen);
        };

        return dfs(root, root->val);
    }
};
