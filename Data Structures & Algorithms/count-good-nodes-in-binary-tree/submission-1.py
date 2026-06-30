# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes_count = 0
        def dfs(root, greatest_seen):
            if not root:
                return None
            
            if root.val >= greatest_seen:
                self.good_nodes_count += 1
                greatest_seen = root.val

            dfs(root.left, greatest_seen)
            dfs(root.right, greatest_seen)

        dfs(root, root.val)
        return self.good_nodes_count