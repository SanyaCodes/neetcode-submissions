# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(x,y):
            if not x and not y:
                return True
            if (not x and y) or (not y and x) or (x.val != y.val):
                return False
            return check(x.left,y.left) and check(x.right,y.right)
        
        def tvl(root,subroot):
            if not root:
                return False
            if check(root,subroot):
                return True
            return tvl(root.left,subroot) or tvl(root.right,subroot)
        
        return tvl(root,subRoot)

        