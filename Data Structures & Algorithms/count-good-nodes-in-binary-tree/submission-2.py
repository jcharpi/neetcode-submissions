# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_seen):
            if not root:
                return 0
            
            count = 1 if root.val >= max_seen else 0
            max_seen = max(max_seen, root.val)

            return count + dfs(root.left, max_seen) + dfs(root.right, max_seen)

        
        return dfs(root, root.val)