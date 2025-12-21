# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValid(self, node: Optional[TreeNode], mxl, mxr) :
        if not (mxl < node.val < mxr) :
            return False

        left_val, right_val = True, True

        if node.left :
            left_val = self.isValid(node.left, mxl, node.val)
        
        if node.right :
            right_val = self.isValid(node.right, node.val, mxr)

        return left_val and right_val

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mxl, mxr = -1<<32, 1<<32
        return self.isValid(root, mxl, mxr)
