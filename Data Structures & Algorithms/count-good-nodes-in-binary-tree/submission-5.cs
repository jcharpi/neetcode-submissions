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
    public int GoodNodes(TreeNode root) {
        int DFS(TreeNode root, int maxSeen) {
            if (root == null) return 0;

            int count = root.val >= maxSeen ? 1 : 0;
            maxSeen = Math.Max(maxSeen, root.val);

            return count + DFS(root.left, maxSeen) + DFS(root.right, maxSeen);
        }

        return DFS(root, root.val);
    }
}
