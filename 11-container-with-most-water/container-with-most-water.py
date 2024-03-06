# 사각형 이니까 (len(height) - i) * (min(height[left], height[right]))
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0

        while left < right :
            currentArea = min(height[left], height[right]) * (right - left)
            ans = max(ans, currentArea)

            if height[left] < height[right] :
                left += 1
            else :
                right -= 1

        return ans