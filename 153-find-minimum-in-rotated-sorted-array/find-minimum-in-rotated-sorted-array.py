class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r :
            mid = (l + r) // 2
            if nums[mid] < nums[(mid + 1) % n] and nums[mid] < nums[(mid - 1) % n] :
                return nums[mid]

            elif nums[mid] < nums[r] :
                r = mid - 1
            
            else :
                l = mid + 1

        return nums[0]