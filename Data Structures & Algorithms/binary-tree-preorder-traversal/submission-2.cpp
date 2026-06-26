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
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> out;
        stack<TreeNode*> s;
        TreeNode* curr = root;

        while (curr || !s.empty()) {
            if (curr) {
                out.push_back(curr->val);
                s.push(curr->right);
                curr = curr->left;
            } else {
                curr = s.top();
                s.pop();
            }
        }
        return out;

    }
};