# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out, queue = [], deque()
        if root:
            queue.append(root)
            out.append([root.val])

        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    level.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    level.append(curr.right.val)
            if level:
                out.append(level)
        return out