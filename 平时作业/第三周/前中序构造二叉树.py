# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build_helper(preorder,inorder):
            if not (preorder and inorder):
                return None
            root=TreeNode(preorder[0])
            mid_i = inorder.index(preorder[0])
            root.left = build_helper(preorder[1:mid_i+1],inorder[:mid_i])
            root.right = build_helper(preorder[mid_i+1:],inorder[mid_i+1:])
            return root
        root = build_helper(preorder,inorder)
        return root