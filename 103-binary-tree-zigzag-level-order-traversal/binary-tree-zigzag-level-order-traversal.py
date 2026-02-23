# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        d = 1

        while q :
            cur_lv = []
            for _ in range(len(q)) :
                cur_node = q.popleft()

                if cur_node :
                    cur_lv.append(cur_node.val)
                    q.append(cur_node.left)
                    q.append(cur_node.right)
            if cur_lv :
                res.append(cur_lv[::d])
            d *= -1

        return res
