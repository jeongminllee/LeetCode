class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(p, q, s) :
            if p == q and p + q == n * 2 :
                res.append(s)
                return
            
            if p < n :
                dfs(p + 1, q, s + '(')
            
            if q < p :
                dfs(p, q + 1, s + ')')

        dfs(0, 0, '')

        return res