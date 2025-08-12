class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == [] :
            return []
        
        if len(nums) == 1 :
            return [f"{nums[0]}"]

        res = []
        tmp = [nums[0], nums[0]]
        i = nums[0]

        for num in nums[1:] :
            i += 1
            if num == i :
                tmp[1] = i
            else :
                if tmp[0] != tmp[1] :
                    res.append(f"{tmp[0]}->{tmp[1]}")
                else :
                    res.append(f"{tmp[0]}")

                tmp = [num, num]
                i = num
        
        tmp[1] = i
        if tmp[0] != tmp[1] :
            res.append(f"{tmp[0]}->{tmp[1]}")
        else :
            res.append(f"{tmp[0]}")

        return res
