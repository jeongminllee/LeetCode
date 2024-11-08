class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()
        for i in range(len(nums)) :
            if nums[i] in set_nums :
                return True
            set_nums.add(nums[i])
        return False

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         set_nums = set(nums)
        
#         return len(set_nums) != len(nums)