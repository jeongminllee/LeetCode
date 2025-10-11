class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = sm = 0
        res = float('inf')

        for right in range(len(nums)) :
            sm += nums[right]
            
            while sm >= target :
                res = min(res, right - left + 1)
                sm -= nums[left]
                left += 1

        return res if res != float('inf') else 0