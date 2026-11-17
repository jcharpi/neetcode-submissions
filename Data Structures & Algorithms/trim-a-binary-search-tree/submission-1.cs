/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */


// given
// preserve relational mapping

// goal
// remove nodes < low and > high

// dsa
// base case:
// if we hit a leaf, return (no operations)

// if a root is < low:
// remove root + left subtree, check if right subtree < low
// - if yes, remove
// - if no, replace root with right subtree root

// if a root is > high:
// remove root + right subtree, check if left subtree > high
// - if yes, remove
// - if no, replace root with right subtree root
public class Solution {
    public TreeNode TrimBST(TreeNode root, int low, int high) {
        TreeNode Dfs(TreeNode root) {
            if (root == null) return root;

            root.left = Dfs(root.left);
            root.right = Dfs(root.right);

            if (root.val < low) {
                return TrimBST(root.right, low, high);
            }

            if (root.val > high) {
                return TrimBST(root.left, low, high);
            }

            return root;
        } 

        return Dfs(root);
    }
}
