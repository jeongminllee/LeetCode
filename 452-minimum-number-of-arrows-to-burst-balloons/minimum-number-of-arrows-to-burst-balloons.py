class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrows = 1
        target = points[0][1]

        for point in points[1:] :
            if target < point[0] :
                target = point[1]
                arrows += 1

        return arrows