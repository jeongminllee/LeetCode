class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        arrI, arrJ = set(), set()
        for i in range(n) :
            for j in range(m) :
                if matrix[i][j] == 0 :
                    arrI.add(i)
                    arrJ.add(j)

        for i in range(n) :
            for j in range(m) :
                if i in arrI or j in arrJ :
                    matrix[i][j] = 0