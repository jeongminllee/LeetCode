class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        idx_k = 0
        for idx_num in range(len(nums)) :
            if dct[nums[idx_num]] < 2 :
                nums[idx_k] = nums[idx_num]
                dct[nums[idx_num]] += 1
                idx_k += 1


        return idx_k