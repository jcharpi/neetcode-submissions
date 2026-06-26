# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, out = [], []
        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                out.append(curr.val)
                curr = curr.right
        return out