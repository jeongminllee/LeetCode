class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right :
            mid = (left + right) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1] :
                break

            elif target > matrix[mid][-1] :
                left = mid + 1
            
            else :
                right = mid - 1

        lst = matrix[mid]
        left = 0
        right = len(lst) - 1

        while left <= right :
            mid = (left + right) // 2

            if target == lst[mid] :
                return True
            elif target > lst[mid] :
                left = mid + 1
            else :
                right = mid - 1

        return False