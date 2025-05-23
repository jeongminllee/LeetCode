from collections import deque
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
        averages = []

        while q :
            level_sum, num_nodes = 0, len(q)
            for _ in range(num_nodes) :
                node = q.popleft()
                level_sum += node.val
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)

            averages.append(level_sum / num_nodes)

        return averages