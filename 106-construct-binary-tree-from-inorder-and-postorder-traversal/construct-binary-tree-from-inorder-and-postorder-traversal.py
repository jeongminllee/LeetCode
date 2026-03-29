# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {v:i for i, v in enumerate(inorder)}
        def helper(s, e) :
            if s > e :
                return

            el = postorder.pop()
            si = index_map[el]
            root = TreeNode(inorder[si])

            root.right = helper(si+1, e)
            root.left = helper(s, si-1)
            return root

        return helper(0, len(inorder)-1)