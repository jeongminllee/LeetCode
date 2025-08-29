class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque()
        q.append((startGene, 0))

        visited = set()
        visited.add(startGene)

        options = ['A', 'C', 'G', 'T']
        cnt = 0

        while q :
            curr, cnt = q.popleft()
            if curr == endGene :
                return cnt

            for option in options :
                for s in range(8) :
                    nxt = curr[:s] + option + curr[s+1:]
                    if nxt in bank and nxt not in visited :
                        visited.add(nxt)
                        q.append((nxt, cnt + 1))
        return -1   