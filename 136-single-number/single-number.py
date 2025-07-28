class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        for num in nums :
            dct[num] += 1

        for num in nums :
            if dct[num] == 1 :
                return num