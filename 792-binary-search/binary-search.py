class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums.sort() # 만약 sorted가 되어 있지 않다면.
        s, e = 0, len(nums) - 1
        while s <= e :
            mid = (s + e) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                e = mid - 1
            else :
                s = mid + 1
        return -1