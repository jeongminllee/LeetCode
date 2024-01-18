def bisect_left(a, x) :
    l, r = 0, len(a)
    while l < r :
        mid = (l + r) // 2
        if a[mid] < x :
            l = mid + 1
        else :
            r = mid
    return l
            
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for x in nums :
            if not dp or x > dp[-1] :
                dp.append(x)
            else :
                idx = bisect_left(dp, x)
                dp[idx] = x
        return len(dp)