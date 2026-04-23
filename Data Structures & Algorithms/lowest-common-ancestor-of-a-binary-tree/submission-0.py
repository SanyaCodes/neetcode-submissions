# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def tvl(node, p, q):
            if not node or node == p or node == q:
                return node
            left = tvl(node.left, p, q)
            right = tvl(node.right, p, q)
            if left and right:
                return node
            return left or right
        
        return tvl(root, p, q)

        