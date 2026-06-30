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
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode FindAncestor(TreeNode root) {
            if (root == null) return null;

            if (p.val < root.val && q.val < root.val) return FindAncestor(root.left);
            else if (p.val > root.val && q.val > root.val) return FindAncestor(root.right);
            else return root;
        }

        return FindAncestor(root);
    }
}
