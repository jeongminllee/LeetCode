"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # Node : val, isLeaf, topLeft, topRight, bottomLeft, bottomRight
        node = Node(False, True, None, None, None, None)
        n = len(grid)
        if n == 1 :
            node.val = True if grid[0][0] == 1 else False
            return node
        
        return self.checkLeaf(grid, 0, 0, n)

    def checkLeaf(self, grid : List[List[int]], sr: int, sc: int, leng: int) :
        sm = 0

        for row in grid[sr:sr+leng] : 
            col = row[sc:sc+leng]
            for v in col :
                sm += v

        # 1로만 구성됨
        if sm == leng * leng:
            return Node(True, True, None, None, None, None)
        # 0으로만 구성됨
        elif sm == 0 :
            return Node(False, True, None, None, None, None)
        else :
            return Node(True, False, 
                        self.checkLeaf(grid, sr, sc, leng//2),
                        self.checkLeaf(grid, sr, sc+leng//2, leng//2),
                        self.checkLeaf(grid, sr+leng//2, sc, leng//2),
                        self.checkLeaf(grid, sr+leng//2, sc+leng//2,leng//2),)