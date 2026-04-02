class Vertex :
    def __init__(self, v):
        self.v = v              # 과목 번호
        self.incoming = []      # v 과목의 선행 과목들
        self.outgoing = []      # v 과목을 선행으로 필요로 하는 다음 과목들

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 과목 번호 -> Vertex 객체
        vertexes = {}

        # [to, fr] : to 과목을 들으려면 fr 과목을 먼저 들어야 함
        for to, fr in prerequisites :
            # 그래프에 fr 과목에 해당하는 정점(Vertex 객체)을 생성하지 않았으면 생성
            if fr not in vertexes.keys() :
                vertexes[fr] = Vertex(fr)   # class Vertex에서 val = fr, incoming = [], outgoing = []
            
            # 그래프에 to 과목에 해당하는 정점(Vertex 객체)을 생성하지 않았으면 생성
            if to not in vertexes.keys() :
                vertexes[to] = Vertex(to)   # class Vertex에서 val = to, incoming = [], outgoing = []

            # fr -> to 간선 추가
            vertexes[fr].outgoing.append(to)    # vertexes{fr : Vertex(val=fr, incoming=[], outgoing=[to])}    추가 되는 것만 작성함
            vertexes[to].incoming.append(fr)    # vertexes{to : Vertex(val=to, incoming=[fr], outgoing=[])}    추가 되는 것만 작성함

        q = deque()

        for vertex in list(vertexes.values()) : # Vertex() 클래스만 땡겨옴.
            if len(vertex.incoming) == 0 :      # Vertex.incoming = [] => 선행 과목이 없는 수업이므로 바로 수강 가능
                q.append(vertex)

        while q :
            vertex = q.popleft()    # 선행과목이 없는 수업부터 처리
            cur = vertex.v           # 현재 바로 수강 가능한 과목

            for to in vertex.outgoing :             # 현재 과목을 선수과목을 필요로 하는 다음 과목들
                vertexes[to].incoming.remove(cur)    # Vertext(val=to, incoming=[fr 삭제], outgoing=[])

                if len(vertexes[to].incoming) == 0 :    # 선행이 다 완료했으면
                    q.append(vertexes[to])              # 이제 수강 가능한 수업을 큐에 추가

            del vertexes[cur]                        # 수강한 과목을 그래프에서 제거

        return len(vertexes.values()) == 0          # 수업을 모두 깔끔하게 다 들었으면 True 아니면 False