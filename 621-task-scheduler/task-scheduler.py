class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        cnt = 0

        for task in tasks :
            freq[ord(task) - ord("A")] += 1
            cnt = max(cnt, freq[ord(task) - ord("A")])

        time = (cnt - 1) * (n + 1)
        for f in freq :
            if f == cnt :
                time += 1

        return max(len(tasks), time)