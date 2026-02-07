# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)

        res = []

        while q :
            lv_sum, length = 0, len(q)
            for _ in range(length) :
                curr = q.popleft()
                lv_sum += curr.val
                if curr.left :
                    q.append(curr.left)
                if curr.right :
                    q.append(curr.right)

            res.append(lv_sum / length)

        return res