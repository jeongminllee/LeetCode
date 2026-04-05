class Vertex :
    def __init__(self, x) :
        self.x = x
        self.incoming = []
        self.outgoing = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        vertexes = {}

        for to, fr in prerequisites :
            if fr not in vertexes.keys() :
                vertexes[fr] = Vertex(fr)
            if to not in vertexes.keys() :
                vertexes[to] = Vertex(to)

            vertexes[fr].outgoing.append(to)
            vertexes[to].incoming.append(fr)

        q = deque()

        for vertex in list(vertexes.values()) :
            if len(vertex.incoming) == 0 :
                q.append(vertex)

        while q :
            vertex = q.popleft()
            cur = vertex.x

            for nxt in vertex.outgoing :
                vertexes[nxt].incoming.remove(cur)

                if len(vertexes[nxt].incoming) == 0:
                    q.append(vertexes[nxt])

            del vertexes[cur]

        return len(vertexes.values()) == 0 