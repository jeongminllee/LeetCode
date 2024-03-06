class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums) - 2) :
            if i > 0 and nums[i] == nums[i - 1] :
                continue    # Skip duplicate values of the first number
            j, k = i + 1, len(nums) - 1
            while j < k :
                target = nums[i] + nums[j] + nums[k]
                if target > 0 :
                    k -= 1
                elif target < 0 :
                    j += 1
                else : 
                    ans.add((nums[i], nums[j], nums[k]))
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1] :
                        j += 1  # Skip duplicate values of the second number
                    while j < k and nums[k] == nums[k + 1] :
                        k -= 1  # Skip duplicate values of the third number
        return ans


# 1. two-pointer approach

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         ans = set()
#         for i in range(len(nums) - 2) :
#             j = i + 1
#             k = len(nums) - 1
#             while j < k :
#                 target = nums[i] + nums[j] + nums[k]

#                 if target > 0 :
#                     k -= 1
#                 elif target < 0 :
#                     j += 1
#                 else :
#                     ans.add((nums[i], nums[j], nums[k]))
#                     j += 1
#                     k -= 1

#         return ans