# 2차원 배열 안에 target 이 있냐는 문제임.
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# 두 가지 조건을 성립하는 m * n 크기의 행렬이 존재한다.
# 반드시 O(log(m * n))의 시간복잡도를 써야한다.
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