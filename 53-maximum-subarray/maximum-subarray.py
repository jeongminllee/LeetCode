class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]   # nums.length가 최소 1이기 때문에 가장 처음 수로 설정
        tmp = 0

        for i in range(len(nums)) :
            if tmp < 0 :
                tmp = 0
            tmp += nums[i]  # 0에다가 nums[i]를 더함
            res = max(res, tmp)

        return res