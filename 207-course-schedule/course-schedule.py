class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]     # graph[i] : 과목 i를 선수과목으로 가지는 다음 과목들
        indegree = [0] * numCourses                 # indegree[i] : 과목 i의 진입 차수, 즉 선수과목 개수

        for to, fr in prerequisites :
            graph[fr].append(to)            # fr -> to 간선 추가
            indegree[to] += 1               # to 과목의 선수과목 수 (진입 차수) 1 증가

        q = deque()

        for i in range(numCourses) :        
            if indegree[i] == 0 :           # 선수과목이 하나도 없으면 지금 바로 수강 가능
                q.append(i)                 # 수강 가능하므로 큐에 추가
    
        taken = 0                           # 위상 정렬로 처리 완료한 과목 수(수업 몇개 들었니?)

        while q :                           # 현재 바로 들을 수 있는 수업을 들어보자.
            cur = q.popleft()               # 지금 수강 가능한 과목 하나 꺼내 처리 시작
            taken += 1                      # 해당 과목 처리 완료

            for nxt in graph[cur] :         # cur를 선수과목으로 가지는 후속 과목들
                indegree[nxt] -= 1          # nxt 입장에서 필요한 선수과목 하나가 충족됨
                if indegree[nxt] == 0 :     # nxt 수업을 듣기 위한 선수과목이 모두 충족되면
                    q.append(nxt)           # 수강 가능하므로 큐에 추가

        return taken == numCourses          # 모든 과목을 처리했으면 True, 아니면 False