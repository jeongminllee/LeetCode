class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = ans = last = 0

        for i in range(len(nums) - 1) :
            goal = max(goal, nums[i] + i)

            if i == last :
                last = goal
                ans += 1
        return ans