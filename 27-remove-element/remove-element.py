class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums에서 val과 같지 않은 수가 얼마만큼 포함되어 있는지 찾는 문제
        # + nums 배열을 0번부터 위 조건에 해당되는 수로 나열
        i = 0
        for j in range(len(nums)) :
            if val != nums[j] :
                nums[i] = nums[j]
                i += 1
        
        return i