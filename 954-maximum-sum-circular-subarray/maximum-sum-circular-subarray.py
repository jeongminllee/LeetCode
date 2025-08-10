class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = min_sum = curr_max_sum = curr_min_sum = total = nums[0]

        for num in nums[1:] :
            curr_min_sum = min(curr_min_sum + num, num)
            min_sum = min(curr_min_sum, min_sum)

            curr_max_sum = max(curr_max_sum + num, num)
            max_sum = max(curr_max_sum, max_sum)

            total += num

        circular = total - min_sum

        if circular == 0 :
            return max_sum
            
        return max(circular, max_sum)