class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = cnt = 1

        for i in range(1, len(nums)) :
            if nums[i-1] == nums[i] :
                cnt += 1
            else :
                cnt = 1

            if cnt <= 2 :
                nums[k] = nums[i]
                k += 1

        return k