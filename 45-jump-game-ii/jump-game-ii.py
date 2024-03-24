class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = 0
        ans = 0
        last = 0

        for i in range(len(nums) - 1) :
            goal = max(goal, i + nums[i])

            if i == last :
                last = goal
                ans += 1

        return ans