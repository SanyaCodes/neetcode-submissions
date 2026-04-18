# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # using inorder traversal
        
        def postorder_with_nulls(root, out):
            if not root:
                out.append(None)
                return
            postorder_with_nulls(root.left, out)
            postorder_with_nulls(root.right, out)
            out.append(root.val)

        def isSameTree(p, q):
            t1, t2 = [], []
            postorder_with_nulls(p, t1)
            postorder_with_nulls(q, t2)
            return t1 == t2

        return isSameTree(p,q)

        