class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        hash_table = {}

        for idx, val in enumerate(nums):
            bkt = val // (valueDiff+1)
            if (bkt in hash_table and idx - hash_table[bkt][0] <= indexDiff) or \
                (bkt-1 in hash_table and idx - hash_table[bkt-1][0] <= indexDiff and abs(val - hash_table[bkt-1][1]) <= valueDiff) or \
                    (bkt+1 in hash_table and idx - hash_table[bkt+1][0] <= indexDiff and abs(val - hash_table[bkt+1][1]) <= valueDiff):
                return True

            hash_table[bkt] = (idx, val)

        return False