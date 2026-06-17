# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        def get_successor_val(root):
            if not root.left:
                return root.val
            return get_successor_val(root.left)
            
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left and root.right:
                # 2 children: replace root with successor, then delete successor in subtree
                root.val = get_successor_val(root.right)
                root.right = self.deleteNode(root.right, root.val)
            elif root.left or root.right:
                # 1 child: replace root with its child
                return root.left if root.left else root.right
            else:
                # no children: delete root
                return None

        return root