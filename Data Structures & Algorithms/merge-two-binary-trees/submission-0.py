# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def add(p,q):
            if not p and not q:
                return
            if not p:
                return q
            if not q:
                return p
            
            p.val = p.val+q.val
            p.left = add(p.left,q.left)
            p.right = add(p.right,q.right)   
            return p

        
        return add(root1,root2)


            
        