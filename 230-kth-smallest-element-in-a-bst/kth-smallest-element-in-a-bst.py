# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        dt = []
        self.inorder(root, dt)
        return dt[k-1]

    def inorder(self, root, dt) :
        if root.left :
            self.inorder(root.left, dt)

        dt.append(root.val)

        if root.right :
            self.inorder(root.right, dt)