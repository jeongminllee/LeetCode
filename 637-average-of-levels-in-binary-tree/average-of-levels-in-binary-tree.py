# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dummy = root
        q = deque()
        q.append(dummy)
        averages = []

        while q :
            lv_sum, length = 0, len(q)
            for _ in range(length) :
                node = q.popleft()
                lv_sum += node.val
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)

            averages.append(lv_sum / length)

        return averages