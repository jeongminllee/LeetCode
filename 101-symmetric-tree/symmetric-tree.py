
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(p, q) :
            if not p and not q :
                return True

            if not p or not q or p.val != q.val :
                return False

            return check(p.left, q.right) and check(p.right, q.left)

        return check(root.left, root.right)
'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [root.left, root.right]

        while stack :
            q = stack.pop()
            p = stack.pop()

            if not p and not q :
                continue
            if not p or not q or p.val != q.val :
                return False

            stack.append(p.left)
            stack.append(q.right)
            stack.append(p.right)
            stack.append(q.left)

        return True

'''