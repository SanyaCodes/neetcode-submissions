# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(root):
            temp = root.left
            root.left = root.right
            root.right = temp
            return root
        
        def pre(root):
            if not root:
                return
            invert(root)
            pre(root.left)
            pre(root.right)
        
        pre(root)
        return root

        