class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # 전체 합이 홀수이면 두 개의 동일한 부분집합으로 나눌 수 없습니다.
        if total_sum % 2 != 0 :
            return False

        target = total_sum // 2
        dp = set([0])

        for num in nums :
            next_dp = set()
            for t in dp :
                if t + num == target :
                    return True
                next_dp.add(t + num)
                next_dp.add(t)
            dp = next_dp

        return target in dp