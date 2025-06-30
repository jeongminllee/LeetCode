# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root :
            print(f"Visited null node.")
            return None
        print(f"Visited Node {root.val}")

        if root == p :
            print(f"Found p: {p.val}")
            return root
        if root == q :
            print(f"Found q: {q.val}")
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right :
            print(f"LCA found at Node {root.val}")
            return root

        return left or right