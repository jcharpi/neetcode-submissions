# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # lowest node in dfs that covers both nodes?

        def find_ancestor(root):
            if not root:
                return None
            
            if p.val < root.val and q.val < root.val:
                return find_ancestor(root.left)
            elif p.val > root.val and q.val > root.val:
                return find_ancestor(root.right)
            else:
                return root

        return find_ancestor(root)