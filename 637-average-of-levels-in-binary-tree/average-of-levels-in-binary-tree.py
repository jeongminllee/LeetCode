# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dummy = root
        idx = 0
        lst = [[] for _ in range(10**4 + 1)]
        res = []

        self.average_tree(dummy, 0, lst)

        print(lst)
        while lst[idx] :
            length = len(lst[idx])
            res.append(sum(lst[idx]) / length)
            idx += 1
        
        return res
        

    def average_tree(self, tree: Optional[TreeNode], idx: int, lst: List) :
        if tree.left is None and tree.right is None :
            lst[idx].append(tree.val)
            return 

        if tree.left :
            self.average_tree(tree.left, idx+1, lst)
        if tree.right :
            self.average_tree(tree.right, idx+1, lst)

        lst[idx].append(tree.val)
        return
        