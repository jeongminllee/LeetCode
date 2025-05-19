class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 :
            return [-1,-1]
        
        idx = self.binary_search(nums, target)

        if idx == -1 :
            return [-1,-1]

        return self.two_pointer(nums, target, idx)

    def binary_search(self, nums: List[int], target: int) -> int :
        left = 0
        right = len(nums) - 1

        while left <= right :
            mid = (left + right) // 2

            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                right = mid - 1
            else :
                left = mid + 1

        return -1

    def two_pointer(self, nums: List[int], target: int, idx: int) -> List[int] :
        left = right = idx
        while 0 <= left and nums[left] == target :
            left -= 1
        left += 1

        while right <= len(nums) - 1 and nums[right] == target :
            right += 1
        right -= 1

        return [left, right]