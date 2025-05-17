class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)) :
            if nums[i] == target :
                ans.append(i)

        return [min(ans), max(ans)] if ans else [-1, -1]