class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        def binary_search(res, num) :
            left = 0
            right = len(res) - 1

            while left <= right :
                mid = (left + right) // 2
                if res[mid] == num :
                    return mid
                elif res[mid] > num :
                    right = mid - 1
                else : 
                    left = mid + 1

            return left

        for num in nums :
            if not res or res[-1] < num :
                res.append(num)
            else :
                idx = binary_search(res, num)
                res[idx] = num
        print(res)
        return len(res)