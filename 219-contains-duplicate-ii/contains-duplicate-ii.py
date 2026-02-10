class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        # O(n*k) = O(10**5 * 10**5) = O(10**10)
        # 옳은 풀이는 아님
        for i in range(len(nums)) :
            for cnt in range(1, k+1) :
                j = i + cnt
                if j <= len(nums) - 1 and nums[i] == nums[j] :
                    return True

        return False
        '''
        '''
        for i in range(len(nums)) :
            j = i + k
            if j > len(nums) :
                j = len(nums) - 1

            target = nums[i:j+1]
            set_target = set(target)
            if len(target) != len(set_target) :
                return True

        return False
        '''
        sliding_window = {}

        for idx, val in enumerate(nums) :
            if val in sliding_window and idx - sliding_window[val] <= k :
                return True
            sliding_window[val] = idx

        return False