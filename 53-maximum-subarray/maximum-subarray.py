class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]

        mid = len(nums) // 2
        left_max = self.maxSubArray(nums[:mid])
        right_max = self.maxSubArray(nums[mid:])

        left_sum = float('-inf')
        sm = 0
        for i in range(mid-1, -1, -1) :
            sm += nums[i]
            left_sum = max(left_sum, sm)

        right_sum = float('-inf')
        sm = 0
        for i in range(mid, len(nums)) :
            sm += nums[i]
            right_sum = max(right_sum, sm)

        cross_max = left_sum + right_sum

        return max(left_max, right_max, cross_max)
