class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = minSum = currMinSum = currMaxSum = totalSum = nums[0]

        for i in range(1, len(nums)) :
            currMaxSum = max(currMaxSum + nums[i], nums[i])
            maxSum = max(maxSum, currMaxSum)

            currMinSum = min(currMinSum + nums[i], nums[i])
            minSum = min(minSum, currMinSum)

            totalSum += nums[i]

        circularSum = totalSum - minSum

        if circularSum == 0 :
            return maxSum

        return max(maxSum, circularSum)