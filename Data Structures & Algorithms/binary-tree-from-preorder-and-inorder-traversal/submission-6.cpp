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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty() || inorder.empty()) return nullptr;

        TreeNode* root = new TreeNode(preorder[0]);
        int inorder_root_index = find(inorder.begin(), inorder.end(), root->val) - inorder.begin();
        vector<int> preorder_left(preorder.begin() + 1, preorder.begin() + 1 + inorder_root_index);
        vector<int> preorder_right(preorder.begin() + inorder_root_index + 1, preorder.end());
        vector<int> inorder_left(inorder.begin(), inorder.begin() + inorder_root_index);
        vector<int> inorder_right(inorder.begin() + inorder_root_index + 1, inorder.end());

        root->left = buildTree(preorder_left, inorder_left);
        root->right = buildTree(preorder_right, inorder_right);

        return root;
    }
};
