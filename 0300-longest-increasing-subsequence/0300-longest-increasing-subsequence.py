def bisect_left(a, x) :     # 이진 탐색을 사용함 (O(logN))
    l, r = 0, len(a)        # 좌측을 0, 우측을 len(a)로 초기화
    while l < r :           # 좌측이 우측보다 작을 때까지 반복
        mid = (l + r) // 2
        if a[mid] < x :     # 중간값이 찾고자 하는 값보다 작으면
            l = mid + 1
        else :
            r = mid
    return l

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for x in nums :
            if not dp or x > dp[-1] :    # dp가 비어있거나, 현재 값이 dp의 마지막 값보다 크다면
                dp.append(x)             # dp에 추가
            else :
                idx = bisect_left(dp, x) # dp에 x가 들어갈 위치를 찾음
                dp[idx] = x              # dp에 x를 추가
        return len(dp)