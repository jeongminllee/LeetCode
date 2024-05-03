class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        half = sum(nums) / 2
        
        for n in nums :
            for s in dp.copy() :
                if s + n <= half :
                    dp.add(s + n)
            dp.add(n)

            if half in dp :
                return True

        return False