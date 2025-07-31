class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = defaultdict(list)
        for i in range(len(nums)) :
            dct[nums[i]].append(i)

        for key, val in dct.items() :
            if len(val) == 1 :
                return key