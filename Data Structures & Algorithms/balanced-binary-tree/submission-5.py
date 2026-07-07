# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (0, True)

            left, right = dfs(root.left), dfs(root.right)
            isTreeBalanced = left[1] and right[1] and abs(left[0] - right[0]) < 2

            return (1 + max(left[0], right[0]), isTreeBalanced)
        
        return dfs(root)[1]