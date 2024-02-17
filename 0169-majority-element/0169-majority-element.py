class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for num in nums :
            if cnt == 0:
                majority_num = num
            cnt += 1 if num == majority_num else -1
        return majority_num
        