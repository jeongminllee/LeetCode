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
        

'''
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        def dfs(n, sums) :
            if n == 1 and 0 in sums : 
                return [max(sums, key = abs)]
            cands = []

            d = sums[1] - sums[0]

            for dr in [1, -1] :
                cnt = Counter(sums)
                new = []
                if cnt[0] == 0 :
                    return []
                for num in sums[::-dr] :
                    if cnt[num] == 0 :
                        continue
                    if cnt[num - d * dr] == 0 :
                        break
                    cnt[num] -= 1
                    new += [num]
                    cnt[num - d*dr] -= 1

                if len(new) == 1 << (n - 1) :
                    cands += [[-d*dr] + dfs(n - 1, new[::-dr])]

            return max(cands, key = len) if cands else []

        sums = sorted(sums)
        return dfs(n, sums)
'''