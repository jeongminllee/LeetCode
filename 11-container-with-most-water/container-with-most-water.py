class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        left, right = 0, len(height) - 1

        while left < right :
            mx = max(mx, (right - left) * min(height[left], height[right]))

            if height[left] > height[right] :
                right -= 1
            else :
                left += 1
        
        return mx