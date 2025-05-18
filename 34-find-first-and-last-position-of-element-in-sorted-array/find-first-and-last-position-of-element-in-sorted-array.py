class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        
        idx = self.binary_search(nums, target)

        if idx == -1 :
            return [-1, -1]
        
        return self.two_pointer(nums, target, idx)

    def binary_search(self, nums, target) :
        left, right = 0, len(nums) - 1

        while left <= right :
            mid = (left + right) // 2
            
            if target == nums[mid] :
                return mid  
            elif target > nums[mid] :
                left = mid + 1
            else :
                right = mid - 1
        
        return -1

    def two_pointer(self, nums, target, idx) :
        left, right = idx, idx

        while 0 <= left and nums[left] == target :
            left -= 1
        left += 1

        while right <= len(nums) - 1 and nums[right] == target :
            right += 1
        right -= 1

        return [left, right]