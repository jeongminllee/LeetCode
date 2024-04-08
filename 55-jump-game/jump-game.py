class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal = last index
        goal = len(nums) - 1

        # last index - 1 부터 돌면서
        for i in range(len(nums)-2, -1, -1) :
            
            if i + nums[i] >= goal :
                goal = i

        return goal == 0