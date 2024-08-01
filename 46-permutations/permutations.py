class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []  # 결과를 저장할 리스트

        # 백트래킹을 위한 헬퍼 함수 정의
        def backtrack(start):
            # 기본 케이스: 모든 숫자를 사용하여 하나의 순열을 완성한 경우
            if start == len(nums):
                result.append(nums[:])  # 현재 순열을 결과 리스트에 추가
                return

            # 순열을 생성하기 위해 start부터 끝까지 각 숫자를 순서대로 시도
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # 현재 위치와 i 위치의 숫자를 교환
                backtrack(start + 1)  # 다음 위치에 대해 백트래킹 호출
                nums[start], nums[i] = nums[i], nums[start]  # 교환한 숫자를 원래 위치로 복원

        backtrack(0)  # 백트래킹 함수 호출 시작, 시작 위치는 0
        return result  # 결과 리스트 반환