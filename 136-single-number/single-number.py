class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Linear runtime complexity 
        # constant extra space 는 무슨말이여
        # 상수 ?? 공간??
        res = 0
        for num in nums :
            res ^= num
        return res