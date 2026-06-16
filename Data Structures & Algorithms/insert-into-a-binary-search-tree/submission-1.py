# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Doesn't need to be balanced
        # Base case: compare with root, see if proper children exist, if not put node there
        # else keep traversing
        #
        # case of 6:
        # does 5 have right node? yes
        # 6 > 5 so check right subtree
        # Does 9 have left subtree? No place node there

        # finds parent node of to-be inserted child, given root
        def traverse(root):
            if not root:
                return None

            if root.right and val > root.val:
                return traverse(root.right)
            elif root.left and val < root.val:
                return traverse(root.left)

            return root

        parent = traverse(root)
        if not parent:
            return TreeNode(val)
        elif val > parent.val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
        
        return root
        
            