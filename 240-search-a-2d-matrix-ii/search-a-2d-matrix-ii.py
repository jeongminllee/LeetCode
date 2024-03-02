class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i = m - 1
        j = 0

        while j < n and i >= 0 :
            if matrix[i][j] == target :
                return True
            elif matrix[i][j] > target :
                i -= 1
            else :
                j += 1

        return False