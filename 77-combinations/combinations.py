class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(n+1)]
        visited = [False for _ in range(n+1)]
        res = []
        self.combinations(1, k, nums, visited, [], 0, res)

        return res

    def combinations(self, bgn, end, nums, visited, buildings, depth, res) :
        if depth == end :
            res.append(buildings[:])
            return

        for idx in range(bgn, len(nums)) :
            if visited[idx] :
                continue

            visited[idx] = True
            self.combinations(idx+1, end, nums, visited, buildings + [nums[idx]], depth + 1, res)
            visited[idx] = False
