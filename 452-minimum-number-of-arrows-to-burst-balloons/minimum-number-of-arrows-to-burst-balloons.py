class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        cnt = 1
        end = points[0][1]

        for ball in points[1:] :
            if ball[0] > end :
                cnt += 1
                end = ball[1]
            else :
                end = min(end, ball[1])

        return cnt