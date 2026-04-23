# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
                #         [1,2,3,4] [2,1,3,4]

                # [2] [2]                     [3,4] [3,4]                 

                #                                     [4] [4]

        if not preorder and not inorder:
            return
        
        root = TreeNode(preorder[0])
        split = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:split+1], inorder[:split])
        root.right = self.buildTree(preorder[split+1:], inorder[split+1:])

        return root