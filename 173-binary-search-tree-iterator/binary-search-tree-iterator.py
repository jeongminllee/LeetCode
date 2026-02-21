# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.dt = []
        self.idx = 0
        self.tree_node(root)

    def next(self) -> int:
        i = self.idx
        self.idx += 1

        return self.dt[i]
            
    def hasNext(self) -> bool:
        return self.idx < len(self.dt)
        

    def tree_node(self, root: Optional[TreeNode]) :
        if root.left :
            self.tree_node(root.left)

        self.dt.append(root.val)
        
        if root.right :
            self.tree_node(root.right)
            

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()