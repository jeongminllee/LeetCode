class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        ans = []

        for n in nums :
            if n in dct :
                dct[n] += 1
            else :
                dct[n] = 1

        sort_dct = sorted(dct.items(), key=lambda x:x[1], reverse=True)

        for i in range(k) :
            ans.append(sort_dct[i][0])
        
        return ans