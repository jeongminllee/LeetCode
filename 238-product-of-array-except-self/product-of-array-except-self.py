class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        left = 1
        right = 1

        for i in range(n) :
            res[i] *= left
            left *= nums[i]

            res[(n-1)-i] *= right
            right *= nums[(n-1)-i]

        return res