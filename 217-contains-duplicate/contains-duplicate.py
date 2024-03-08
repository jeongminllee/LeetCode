class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums :
            if num in hashmap and hashmap[num] >= 1 :
                return True
            hashmap[num] = hashmap.get(num, 0) + 1
        return False