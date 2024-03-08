class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        ans = 0

        for n in hashmap :
            if (n - 1) not in hashmap :
                cnt = 1
                while (n + cnt) in hashmap :
                    cnt += 1

                ans = max(cnt, ans)
        return ans