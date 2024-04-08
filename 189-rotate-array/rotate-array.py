class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        d = k % n
        nums[:] = nums[-d:] + nums[:-d]


# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         if k == 0 :
#             return
#         elif n > k :
#             nums[:] = nums[-k:] + nums[:(n - k)]
#         else :
#             for i in range(k) :
#                 rotation = nums[:-1]
#                 rotation.insert(0, nums[-1])
#                 nums[:] = rotation