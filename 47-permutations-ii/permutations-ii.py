class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, visited):
            if len(path) == n :
                res.append(path[:])
                return

            for i in range(n) :
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]) :
                    continue

                visited[i] = 1
                path.append(nums[i])

                backtrack(path, visited)

                visited[i] = 0
                path.pop()

        n = len(nums)
        nums.sort()
        res = []
        visited = [0] * n
        backtrack([], visited)
        return res