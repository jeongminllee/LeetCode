class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # goal = last index
        goal = len(nums) - 1

        # last index - 1 부터 돌면서
        for i in range(len(nums)-2, -1, -1) :
            # 현재 위치 + 위치에서 이동할 수 있는 거리 >= 마지막 인덱스라면
            if i + nums[i] >= goal :
                # 해당 위치의 인덱스로 goal을 바꾼다.
                goal = i

        return goal == 0