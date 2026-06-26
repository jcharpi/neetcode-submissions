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
class BSTIterator {
private:
    stack<TreeNode*> s;

    void _push_left(TreeNode* node) {
        while (node) {
            s.push(node);
            node = node->left;
        }
    }
public:


    BSTIterator(TreeNode* root) {
        _push_left(root);
    }
    
    int next() {
        TreeNode* out = s.top();
        s.pop();
        _push_left(out->right);
        return out->val;
    }
    
    bool hasNext() { return !s.empty(); }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */