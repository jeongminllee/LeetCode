class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums) - 2) :
            j = i + 1
            k = len(nums) - 1
            while j < k :
                target = nums[i] + nums[j] + nums[k]

                if target > 0 :
                    k -= 1
                elif target < 0 :
                    j += 1
                else :
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

        return ans