class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        ans = []

        for num in nums :
            counter[num] += 1

        sort_cnt = sorted(counter.items(), key=lambda x:x[1], reverse=True)

        for i in range(k) :
            ans.append(sort_cnt[i][0])

        return ans