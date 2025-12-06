class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        target = []
        
        for i in range(n) :
            for j in range(m) :
                if matrix[i][j] == 0 :
                    target.append((i, j))
        
        for i, j in target :
            for a in range(n) :
                matrix[a][j] = 0
            
            for b in range(m) :
                matrix[i][b] = 0

        