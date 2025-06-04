class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 반드시 시간 O(log n) 으로 풀이할 것 => 여기서 이분탐색 등 을 생각할 수 있었음
        # 답(최저값)을 몰라도 찾을 수 가 있나...?
        # 부등호 설정할 때 이상, 이하, 초과, 미만 설정이 어렵다.
        left = 0
        right = len(nums) - 1

        while left < right :
            mid = (left + right) // 2
            if nums[mid] > nums[right] :
                left = mid + 1
            else :
                right = mid
        
        return nums[left]