class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n-2) :
            if i > 0 and nums[i] == nums[i-1] :
                continue

            j = i + 1
            k = n - 1

            while j < k :
                target = nums[i] + nums[j] + nums[k]
                if target == 0 :
                    res.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k :
                        j += 1
                    while nums[k] == nums[k + 1] and j < k :
                        k -= 1
                        
                elif target > 0 :
                    k -= 1
                else :
                    j += 1

        return res