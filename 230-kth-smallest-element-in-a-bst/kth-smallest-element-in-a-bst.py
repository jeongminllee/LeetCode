# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        print(f'Starting with k = {k}')

        while True :
            while root :
                stack.append(root)
                print(f'Push to stack : {root.val}')
                root = root.left

            root = stack.pop()
            print(f'Pop from stack : {root.val}')
            k -= 1
            print(f'k is now : {k}')
            if k == 0 :
                print(f'Found answer : {root.val}')
                return root.val
            
            root = root.right