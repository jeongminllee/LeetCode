# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(node) :
            if not node :
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        vals = inorder(root)
        min_diff = 1 << 32
        for i in range(1, len(vals)) :
            min_diff = min(min_diff, vals[i] - vals[i-1])
        return min_diff