# n의 길이를 가지는 배열 조합을 sums배열의 숫자 중 뽑아서 조합했더니
# 그 배열의 합이 sums 배열 요소 중 하나인 값을 반환함
# ex) n = 3, sums = [-3, -2, -1, 0, 0, 1, 2, 3]
# 이면 저 중 3개를 뽑는다 => [1, 2, -3], 합은 0, sums 배열 내에 0이라는 숫자가 존재.. 정답
# 만약 [-1, -2, 3]이 었다면? 이도 정답으로 인정... 따라서 중복 정답이 존재한다.
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        ans = []
        sums.sort()
        
        while len(sums) > 1 :
            num = sums[-1] - sums[-2]
            countMap = Counter(sums)
            excluding = []
            including = []

            for x in sums :
                if countMap.get(x) > 0 :
                    excluding.append(x)
                    including.append(x + num)
                    countMap[x] -= 1
                    countMap[x + num] -= 1

            if 0 in excluding :
                sums = excluding
                ans.append(num)
            else :
                sums = including
                ans.append(-num)

        return ans