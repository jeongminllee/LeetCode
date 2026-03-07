# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0

        # get height of the tree
        height = 0
        curr = root
        while curr.left :
            curr = curr.left
            height += 1

        # max number of leaves at last level
        maxi = 2 ** height

        # check if particular leaf at the last level exists
        # leaf is a number in [1..2^height]
        # O(logN)
        def exists(leaf: int) -> bool :
            curr = root
            l, r = 1, maxi
            while l < r :
                mid = (l + r) // 2
                if leaf > mid :
                    curr = curr.right
                    l = mid + 1
                else :
                    curr = curr.left
                    r = mid

            return curr is not None

        # binary search the number of leaves at last level
        # BS is O(logN), calling 'exists' on every step makes total TC O(logN * logN)
        l, r = 1, maxi
        while l <= r :
            mid = (l + r) // 2

            if exists(mid) :
                l = mid + 1
            else :
                r = mid - 1

        # 2 ** height - 1 is the number of nodes in the tree without the last level
        # r is the number of leaves at the last level
        return 2 ** height - 1 + r