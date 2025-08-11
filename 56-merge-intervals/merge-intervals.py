class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        temp = [intervals[0][0], intervals[0][1]]
        for inter in intervals[1:] :
            if temp[0] <= inter[0] <= temp[1] :
                temp[0] = min(temp[0], inter[0])
                temp[1] = max(temp[1], inter[1])
            else :
                res.append(temp)
                temp = [inter[0], inter[1]]

        res.append(temp)
        return res