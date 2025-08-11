class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums :
            return []

        res = []
        i = nums[0]
        ans = [i, i]

        if len(nums) == 1 :
            return [f'{nums[0]}']

        for num in nums :
            if num == i :
                ans[1] = i
                i += 1
            else :
                if ans[0] == ans[1] :
                    res.append(f'{ans[0]}')
                else :
                    res.append(f'{ans[0]}->{ans[1]}')
                
                ans[0] = num
                ans[1] = num
                i = num + 1
        # print(ans)
        if ans[0] == ans[1] :
            res.append(f'{ans[0]}')
        else :
            res.append(f'{ans[0]}->{ans[1]}')

        return res