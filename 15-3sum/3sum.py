# 3. defaultdict

# from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negative = defaultdict(int)
        positive = defaultdict(int)
        zeros = 0
        for num in nums :
            if num < 0 :
                negative[num] += 1
            elif num > 0 :
                positive[num] += 1
            else :
                zeros += 1

        res = []
        if zeros :
            for n in negative :
                if -n in positive :
                    res.append((0, n, -n))
            if zeros > 2 :
                res.append((0, 0, 0))

        for set1, set2 in ((negative, positive), (positive, negative)) :
            set1items = list(set1.items())
            for i, (j, k) in enumerate(set1items) :
                for j2, k2 in set1items[i:] :
                    if j != j2 or (j == j2 and k > 1) :
                        if -j -j2 in set2 :
                            res.append((j, j2, -j-j2))
        
        return res



# 2. Skip duplicate values of numbers
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         ans = set()
#         for i in range(len(nums) - 2) :
#             if i > 0 and nums[i] == nums[i - 1] :
#                 continue    # Skip duplicate values of the first number
#             j, k = i + 1, len(nums) - 1
#             while j < k :
#                 target = nums[i] + nums[j] + nums[k]
#                 if target > 0 :
#                     k -= 1
#                 elif target < 0 :
#                     j += 1
#                 else : 
#                     ans.add((nums[i], nums[j], nums[k]))
#                     j, k = j + 1, k - 1
#                     while j < k and nums[j] == nums[j - 1] :
#                         j += 1  # Skip duplicate values of the second number
#                     while j < k and nums[k] == nums[k + 1] :
#                         k -= 1  # Skip duplicate values of the third number
#         return ans


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