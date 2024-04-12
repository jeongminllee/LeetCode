# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: Optional[TreeNode]) -> bool:
        if root is None :
            return 0
        leftValue = self.height(root.left)
        rightValue = self.height(root.right)

        if leftValue == -1 or rightValue == -1 or abs(leftValue - rightValue) > 1 :
            return -1
        
        return 1 + max(leftValue, rightValue)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        answer = self.height(root)
        if answer != -1 :
            return True
        return False