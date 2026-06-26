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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> out;
        if (!root) return out;

        stack<pair<TreeNode*, bool>> s;
        s.push({root, false});
        while (!s.empty()) {
            TreeNode* curr = s.top().first;
            bool visited = s.top().second;
            s.pop();

            if (visited) {
                out.push_back(curr->val);
            } else {
                s.push({curr, true});
                if (curr->right) s.push({curr->right, false});
                if (curr->left) s.push({curr->left, false});
            }
        }
        return out;
    }
};