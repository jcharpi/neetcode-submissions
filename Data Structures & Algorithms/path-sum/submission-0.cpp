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
    int currentSum = 0;
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (!root) return false;
        currentSum += root->val;

        if (currentSum == targetSum && !root->left && !root->right) return true;
        if (hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum)) return true;
        currentSum -= root->val;
        return false;
    }
};