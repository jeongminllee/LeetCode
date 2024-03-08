class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        pre = 1
        for i in range(n) :
            ans[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(n - 1, -1, -1) :
            ans[i] *= post
            post *= nums[i]

        return ans

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = [1] * n
#         pre = 1
#         post = 1
#         for i in range(n) :
#             ans[i] *= pre
#             pre *= nums[i]
#             ans[(n - 1) - i] *= post
#             post *= nums[(n - 1) - i]
        
#         return ans