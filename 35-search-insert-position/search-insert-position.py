class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if nums[right] < target :
            return len(nums)

        while left < right :
            mid = (left + right) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                right = mid
            else :
                left = mid + 1

        return left