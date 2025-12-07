class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = 1
        right = 1

        res = [1] * n

        for i in range(n) :
            res[i] *= left
            left *= nums[i]

        for i in range(n-1, -1, -1) :
            res[i] *= right
            right *= nums[i]

        return res
