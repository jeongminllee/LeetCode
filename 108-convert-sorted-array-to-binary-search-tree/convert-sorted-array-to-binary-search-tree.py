# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.convert(nums, 0, len(nums) - 1)

    def convert(self, nums: List[int], idx_left: int, idx_right: int) :
        if idx_left > idx_right :
            return None

        idx_mid = (idx_left + idx_right) // 2
        node = TreeNode(nums[idx_mid])

        node.left = self.convert(nums, idx_left, idx_mid-1)
        node.right = self.convert(nums, idx_mid+1, idx_right)

        return node