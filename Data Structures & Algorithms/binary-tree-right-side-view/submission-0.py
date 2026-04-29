# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        from collections import deque

        def bfs(root):

            r_view = []
            que = deque([root])

            while que:
                level_size = len(que)

                for i in range(level_size):
                    curr = que.popleft()

                    if i==level_size-1: r_view.append(curr.val)

                    if curr.left: que.append(curr.left)
                    if curr.right: que.append(curr.right)
            
            return r_view
        
        return bfs(root)
        