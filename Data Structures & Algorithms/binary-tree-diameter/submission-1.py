# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.dia = 0

        def max_height(node):
            if not node:
                return 0
            left = max_height(node.left)
            right = max_height(node.right)
            self.dia = max(self.dia, left+right)
            return max(left,right)+1
        
        max_height(root)
        return self.dia



        