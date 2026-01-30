class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        board = copy.deepcopy(matrix)

        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]

        d = 0
        res = []
        ci, cj = 0, 0
        res.append(matrix[0][0])
        board[0][0] = '.'
        while len(res) != n * m :
            if 0 <= ci + di[d] < n and 0 <= cj + dj[d] < m and\
                board[ci + di[d]][cj + dj[d]] != '.' :
                res.append(board[ci+di[d]][cj+dj[d]])
                board[ci+di[d]][cj+dj[d]] = '.'
                ci = ci+di[d]
                cj = cj+dj[d]
                
            else :
                d = (d+1)%4

        return res