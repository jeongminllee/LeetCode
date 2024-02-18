class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)) :
            if nums == sorted(nums) :
                return True
            nums = nums[1:] + [nums[0]]
            print(nums)
        return False


# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         ans = 0
#         n = len(nums)
#         for i in range(n) :
#             if nums[(i + 1) % n] >= nums[i] :
#                 pass
#             else :
#                 ans += 1
#                 if ans > 1 :
#                     return False
#         return True