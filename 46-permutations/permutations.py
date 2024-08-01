class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(nums, idx, result) :
            if idx == len(nums) - 1 :
                result.append(nums.copy())
                return
            for i in range(idx, len(nums)) :
                nums[idx], nums[i] = nums[i], nums[idx]
                dfs(nums, idx+1, result)
                nums[idx], nums[i] = nums[i], nums[idx]


        dfs(nums, 0, result)
        return result