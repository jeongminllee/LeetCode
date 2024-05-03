# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        ans = []

        while q :
            r_node = None
            n = len(q)

            for i in range(n) :
                node = q.popleft()
                if node :
                    r_node = node
                    q.append(node.left)
                    q.append(node.right)

            if r_node :
                ans.append(r_node.val)

        return ans
