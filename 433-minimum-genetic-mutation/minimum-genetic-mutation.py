class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        '''
        8자리 문자열로 된 유전자
        4가지의 문자로 구성되어 있음 = "A", "C", "G", "T"
        start -> end 로 바꾸려고 함. 
        2번 예시를 보면 AACCGGTT -> AAACGGTA 로 바꿀려면 몇번 은행에 들어갔다 나와야 되나.
        한 번 바꿀 때 하나의 문자만 변형할 수 있음. -> 이게 은행에 있어야 바꿀 수 있음.
        '''
        bankSet = set(bank)
        options = ['A', 'C', 'G', 'T']

        q = deque()
        q.append(startGene)

        visited = set()
        visited.add(startGene)

        cnt = 0

        while q :
            for i in range(len(q)) :
                gene = q.popleft()
                if gene == endGene :
                    return cnt
                for j in range(8) :
                    for option in options :
                        newGene = gene[:j] + option + gene[j+1:]
                        if newGene in bankSet and newGene not in visited :
                            visited.add(newGene)
                            q.append(newGene)

            cnt += 1

        return -1