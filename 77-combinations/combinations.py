class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        output = []
        def dfs(start) :
            if len(output) == k :
                res.append(output[:])
                return
            
            for idx in range(start, n+1):
                output.append(idx)
                dfs(idx + 1)
                output.pop()

        dfs(1)
        return res