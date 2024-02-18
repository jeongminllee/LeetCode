class Solution:
    def check(self, nums: List[int]) -> bool:
        ans = 0
        n = len(nums)
        for i in range(n) :
            if nums[(i + 1) % n] >= nums[i] :
                pass
            else :
                ans += 1
                if ans > 1 :
                    return False
        return True