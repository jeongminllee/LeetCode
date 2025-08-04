class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 원래는 right = len(nums) - 1 을 해주는데
        # 가장 큰 값이 들어오게 될 경우를 생각해서 -1 을 하지 않음.
        left, right = 0, len(nums)

        while left < right : 
            mid = (left + right) // 2
            if nums[mid] == target :
                return mid
            elif nums[mid] > target :
                right = mid
            else :
                left = mid + 1

        return left