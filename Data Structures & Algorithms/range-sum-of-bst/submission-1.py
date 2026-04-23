# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        count = 0

        def dfs(node, l, h):
            nonlocal count
            if not node:
                return
            if node.val >= l and node.val <= h:
                count += node.val
            dfs(node.left, l, h)
            dfs(node.right, l, h)
        
        dfs(root, low, high)
        return count

        