class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])

        res = 0
        for i in range(n) :
            for j in range(m) :
                matrix[i][j] = int(matrix[i][j])
                res = max(res, matrix[i][j])

                if matrix[i][j] and i and j :
                    tmp = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])
                    matrix[i][j] = tmp + 1
                    res = max(matrix[i][j], res)

        return res ** 2