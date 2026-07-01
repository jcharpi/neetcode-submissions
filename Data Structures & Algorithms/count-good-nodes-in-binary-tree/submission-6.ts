/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    goodNodes(root: TreeNode | null): number {
        const dfs = (root: TreeNode | null, maxSeen: number): number => {
            if (!root) return 0
            const count = root.val >= maxSeen ? 1 : 0
            maxSeen = Math.max(maxSeen, root.val)

            return count + dfs(root.left, maxSeen) + dfs(root.right, maxSeen)
        }

        return dfs(root, root.val)
    }
}
