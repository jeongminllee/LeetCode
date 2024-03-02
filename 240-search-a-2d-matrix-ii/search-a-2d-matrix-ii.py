class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m) :
            if target >= matrix[i][0] and target <= matrix[i][-1] :
                left = 0
                right = n
                while left <= right :
                    mid = (left + right) // 2

                    if target == matrix[i][mid] :
                        return True
                    elif target > matrix[i][mid] :
                        left = mid + 1
                    else :
                        right = mid - 1

        return False