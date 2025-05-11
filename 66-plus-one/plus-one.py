class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1) :
            nxt = digits[i] + 1 # 다음 : 현재에서 + 1
            if nxt != 10 :      # 가장 마지막 자리 숫자에 + 1 을 한 결과가 10이 아니라면
                digits[i] = nxt # 다음 순서로 갱신 후 반환
                return digits
            # 만약 nxt 가 10 이라면
            digits[i] = 0   # 해당 순서를 0으로 만들고 i + 1 을 for문에서 진행시킴
            if i == 0 :     # i가 첫 번째 자리 수를 가리키면
                return [1] + digits # 올림 처리를 한 후 반환