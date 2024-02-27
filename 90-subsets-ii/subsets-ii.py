class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(first = 0, curr = []) :
            output.append(curr[:])

            for i in range(first, n) :
                if i > first and nums[i] == nums[i - 1] :
                    continue
                dfs(i + 1, curr + [nums[i]])

        nums.sort()
        output = []
        n = len(nums)
        dfs()
        return output