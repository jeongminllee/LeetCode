class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        top = 0
        bottom = n - 1

        while top < bottom :
            for col in range(n) :
                tmp = matrix[top][col]
                matrix[top][col] = matrix[bottom][col]
                matrix[bottom][col] = tmp
            top += 1
            bottom -= 1

        for row in range(n) :
            for col in range(row+1, n) :
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = tmp

        return matrix