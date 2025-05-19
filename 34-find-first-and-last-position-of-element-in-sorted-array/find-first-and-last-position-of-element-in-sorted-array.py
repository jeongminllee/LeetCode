class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 :
            return [-1,-1]

        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False)

        return [left, right]

    def binary_search(self, nums: List[int], target: int, is_searching_left: bool) -> List[int]:
        left = 0
        right = len(nums) - 1
        idx = -1

        while left <= right :
            mid = (left + right) // 2

            if nums[mid] == target :
                idx = mid
                if is_searching_left :
                    right = mid - 1
                else :
                    left = mid + 1

            elif nums[mid] > target :
                right = mid - 1

            else :
                left = mid + 1

        return idx