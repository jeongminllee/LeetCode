class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        res = 0
        maxI = waterBlock = 0

        for i in range(1, n) :
            if height[i] >= height[maxI] :
                res += waterBlock
                waterBlock = 0
                maxI = i
            waterBlock += (height[maxI] - height[i])

        end = maxI - 1
        maxI, waterBlock = n-1, 0

        for i in range(n-2, end, -1) :
            if height[i] >= height[maxI] :
                res += waterBlock
                waterBlock = 0
                maxI = i
            waterBlock += (height[maxI] - height[i])

        return res