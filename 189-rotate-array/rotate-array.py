class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        nums[:] = nums[-k:] + nums[:-k]
        
        # for _ in range(k) :
        #     target = nums[-1]
        #     nums[:] = [target] + nums[:-1]