# 두 수의 합의 조합이라 순서는 상관 없고, 합만 맞으면 됨.
# input.length = 100이하 자연수
# 완전 탐색을 돌리면 n! 이니까 안됨. - 맞음.
# 이진 탐색을 생각했었는데 답을 찾는 것이 아니라 조합을 완성시키는 것이기 때문에 사용 불가.
# 백트래킹 - 조합을 완성시키는 것이기 때문에 결국 백트래킹을 활용할 수 밖에 없음

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, comb, total) :
            if total == target :
                output.append(comb[:])
                return
            if i >= n or total > target :
                return

            for idx in range(i, n) :
                if idx > i and candidates[idx] == candidates[idx - 1] :
                    continue

                comb.append(candidates[idx])
                backtrack(idx + 1, comb, total + candidates[idx])
                comb.pop()
        output = []
        n = len(candidates)
        candidates.sort()
        backtrack(0, [], 0)
        return output