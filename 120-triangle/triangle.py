class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # INF = 10 ** 8
        tbl = [[0 for _ in range(i+1)] for i in range(len(triangle))]
        tbl[0][0] = triangle[0][0]

        for i in range(1, len(triangle)) :
            for j in range(i+1) :
                if j == 0 :
                    tbl[i][j] = tbl[i-1][j] + triangle[i][j]
                elif j == i :
                    tbl[i][j] = tbl[i-1][j-1] + triangle[i][j]
                else :
                    tbl[i][j] = min(tbl[i-1][j-1], tbl[i-1][j]) + triangle[i][j]
        return min(tbl[-1])