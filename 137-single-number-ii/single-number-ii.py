class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = defaultdict(int)

        for num in nums :
            dct[num] += 1

        for key,val in dct.items() :
            if val == 1 :
                return key

        return -1