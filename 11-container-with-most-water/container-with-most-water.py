class Solution:
    def maxArea(self, height: List[int]) -> int:
        # n <= 10**5 이기 때문에 이중 for문은 좀 위험하고
        # n ln n 까지 만 가능할듯?
        # 투포인터로 접근해보자
        # nxt 가 더 큰 쪽이 먼저 움직이자 양 쪽을 잡아두고
        left = 0
        right = len(height) - 1
        max_value = 0

        while left < right :
            nxt_value = (right - left) * min(height[right], height[left])
            max_value = max(max_value, nxt_value)

            if height[left] < height[right]:
                left += 1
            else :
                right -= 1

        return max_value