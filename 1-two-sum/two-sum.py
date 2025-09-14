class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}

        for idx in range(len(nums)) :
            num = nums[idx]
            if target - num in num_hash :
                return [idx, num_hash[target - num]]
            num_hash[num] = idx