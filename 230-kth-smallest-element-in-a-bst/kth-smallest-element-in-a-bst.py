# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.res = 0
        self.inorderTraversal(root, k)
        return self.res

    def inorderTraversal(self, node, k) :
        if not node or self.cnt >= k :
            return

        self.inorderTraversal(node.left, k)

        self.cnt += 1
        if self.cnt == k :
            self.res = node.val
            return

        self.inorderTraversal(node.right, k)