class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        hashMap[0] = -1
        sm = 0
        cnt = 0

        for i, val in enumerate(nums) :
            if val == 0 :
                sm = sm - 1
            elif val == 1 :
                sm = sm + 1

            if sm not in hashMap :
                hashMap[sm] = i

            else :
                cnt = max(cnt, i - hashMap[sm])

        return cnt