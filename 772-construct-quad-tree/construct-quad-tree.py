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

        return self.my_construct(grid, 0, 0, n)

    def my_construct(self, grid : List[List[int]], sr, sc, delta) :
        one, zero = False, False

        for row in grid[sr:sr+delta] :
            col = row[sc:sc+delta] 
            for local_v in col :
                if local_v == 0 :
                    zero |= True
                else :
                    one |= True

        # 0 으로만 구성됨
        if one == False and zero == True :
            return Node(False, True, None, None, None, None)
        
        # 1 로만 구성됨
        if one == True and zero == False :
            return Node(True, True, None, None, None, None)

        return Node(True, False, 
                    self.my_construct(grid, sr, sc, delta//2),
                    self.my_construct(grid, sr, sc + delta//2, delta//2),
                    self.my_construct(grid, sr+delta//2, sc, delta//2),
                    self.my_construct(grid, sr+delta//2, sc+delta//2, delta//2),)