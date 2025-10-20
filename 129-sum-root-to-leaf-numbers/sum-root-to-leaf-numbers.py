# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) :
        self.answer = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.answer
        
        
    def dfs(self, node: Optional[TreeNode], value: int) -> int :
        nxt_value = value * 10 + node.val

        if node.left is None and node.right is None :
            self.answer += nxt_value
            return

        if node.left :
            self.dfs(node.left, nxt_value)
        
        if node.right :
            self.dfs(node.right, nxt_value)