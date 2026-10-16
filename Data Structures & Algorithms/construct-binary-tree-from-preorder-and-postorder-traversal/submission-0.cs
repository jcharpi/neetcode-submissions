public class Solution {
    public TreeNode ConstructFromPrePost(int[] preorder, int[] postorder) {
        if (preorder.Length == 0) return null;

        TreeNode root = new TreeNode(preorder[0]);
        if (preorder.Length == 1) return root;

        int rightSubtreeVal = postorder[^2];
        int rightSubtreeIndex = Array.IndexOf(preorder, rightSubtreeVal);
        int leftSubtreeSize = rightSubtreeIndex - 1;

        root.left = ConstructFromPrePost(preorder[1..rightSubtreeIndex], postorder[..leftSubtreeSize]);
        root.right = ConstructFromPrePost(preorder[rightSubtreeIndex..], postorder[leftSubtreeSize..^1]);

        return root;
    }
}
