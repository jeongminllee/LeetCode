class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for to, fr in prerequisites :
            graph[fr].append(to)            # 이 수업을 들었으면 다음 들을 수 있는 수업 리스트에 추가
            indegree[to] += 1               # 해당 수업을 들으려면 선행 수업의 가지수 1 추가

        q = deque()

        for i in range(numCourses) :        
            if indegree[i] == 0 :           # 지금 바로 수업 들을 수 있으면
                q.append(i)                 # 큐에 추가
    
        taken = 0                           # 수업 몇개 들었니?

        while q :                           # 현재 바로 들을 수 있는 수업을 들어보자.
            cur = q.popleft()               # 수강 중
            taken += 1                      # 수강 완료한 코스 1 추가

            for nxt in graph[cur] :         # 다음 들을 수 있는 수업
                indegree[nxt] -= 1          # nxt 수업을 듣기 위한 선행 수업이 하나 줄어들었기 때문에 
                if indegree[nxt] == 0 :     # nxt 수업을 이제 들을 수 있으면
                    q.append(nxt)           # 큐에 추가

        return taken == numCourses          # 들었는 수업이 총 개수와 같은지 체크