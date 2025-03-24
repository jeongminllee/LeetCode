class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        left, right = 0, 0
        res = float('inf')

        for right in range(n) :
            cnt += nums[right]

            while cnt >= target :
                res = min(res, right - left + 1)
                cnt -= nums[left]
                left += 1
        
        return res if res != float('inf') else 0