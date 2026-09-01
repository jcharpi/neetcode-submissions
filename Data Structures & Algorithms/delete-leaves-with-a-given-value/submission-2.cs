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
    public TreeNode RemoveLeafNodes(TreeNode root, int target) {
        TreeNode dfs(TreeNode node) {
            if (node == null) return null;

            node.left = dfs(node.left);
            node.right = dfs(node.right);
            if (node.val == target && node.left == null && node.right == null) return null;

            return node;
        }

        return dfs(root);
    }
}