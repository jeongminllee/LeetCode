class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dct = {}

        for i in range(len(values)) :
            d1, d2 = equations[i]
            v = values[i]

            if d1 not in dct :
                dct[d1] = {}

            dct[d1][d2] = v
            dct[d1][d1] = 1

            if d2 not in dct :
                dct[d2] = {}
            
            dct[d2][d1] = 1 / v
            dct[d2][d2] = 1

        res = []

        for q1, q2 in queries :
            if q1 not in dct :
                res.append(-1)
                continue
            
            rtn = self.dfs(dct, q1, q2, 1, [])
            res.append(rtn)

        return res
    
    def dfs(self, dct, bgn, end, v, visited) :
        for mid in dct[bgn] :
            if mid not in visited :
                if mid == end :
                    v *= dct[bgn][mid]
                    return v
                else :
                    rtn = self.dfs(dct, mid, end, v * dct[bgn][mid], visited + [bgn])
                    if rtn != -1 :
                        return rtn
        return -1