class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = False
        for x in matrix :
            for i in x :
                if i == target :
                    flag = True
        return flag