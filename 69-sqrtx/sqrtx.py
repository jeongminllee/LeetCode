class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right :
            mid = (left + right) // 2
            mid2 = mid**2

            if mid2 == x :
                return mid
            elif mid2 > x :
                right = mid - 1
            else :
                left = mid + 1
        return right