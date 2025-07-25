class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        res = nums[0]
        tmp = 0
        
        for i in range(len(nums)-1, -1, -1) :
            if nums[i] <= 0 :
                tmp = 0
            
            tmp += nums[i]
            res = max(res, tmp)
            
        return res