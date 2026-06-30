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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        function<TreeNode*(TreeNode*)> findAncestor = [&](TreeNode* root) -> TreeNode* {
            if (!root) return nullptr;

            if (p->val < root->val && q->val < root->val) return findAncestor(root->left);
            else if (p->val > root->val && q->val > root->val) return findAncestor(root->right);
            else return root;
        };

        return findAncestor(root);
    }
};
