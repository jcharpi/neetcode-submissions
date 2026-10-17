class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        
        rightTreeStartIndex = preorder.index(postorder[-2])
        leftTreeSize = rightTreeStartIndex - 1
        
        root.left = self.constructFromPrePost(preorder[1:rightTreeStartIndex], postorder[:leftTreeSize])
        root.right = self.constructFromPrePost(preorder[rightTreeStartIndex:], postorder[leftTreeSize:-1])\

        return root