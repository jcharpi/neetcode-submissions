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

public class Solution {
    public bool IsValidBST(TreeNode root) {
        bool dfs(TreeNode root, int low, int high) {
            if (root == null) return true;

            if (root.val <= low || root.val >= high) return false;

            return dfs(root.left, low, root.val) && dfs(root.right, root.val, high);
        }

        return dfs(root, int.MinValue, int.MaxValue);
    }
}
