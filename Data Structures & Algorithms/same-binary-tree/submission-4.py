# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # using inorder traversal
        
        def inorder_with_nulls(root, out):
            if not root:
                out.append(None)
                return
            out.append(root.val)
            
            inorder_with_nulls(root.left, out)
            
            inorder_with_nulls(root.right, out)

        def isSameTree(p, q):
            t1, t2 = [], []
            inorder_with_nulls(p, t1)
            inorder_with_nulls(q, t2)
            return t1 == t2

        return isSameTree(p,q)

        