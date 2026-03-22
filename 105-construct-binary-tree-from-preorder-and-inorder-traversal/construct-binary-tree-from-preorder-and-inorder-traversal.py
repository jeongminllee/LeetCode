# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.idx = 0

        def build(start, end) :
            if start > end :
                return None 

            root_val = preorder[self.idx]
            self.idx += 1
            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)

            return root

        return build(0, len(inorder) - 1)