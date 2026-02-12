class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        n = 10 ** 5
        k = 10 ** 5 
        O(n) 으로 끝내야함. 
        """
        n = len(nums)
        target = {}

        for idx in range(n) :
            if nums[idx] in target and idx - target[nums[idx]] <= k :
                return True

            target[nums[idx]] = idx
        return False
