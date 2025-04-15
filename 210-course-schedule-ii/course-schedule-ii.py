class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incoming_edge = [0 for _ in range(numCourses)]
        edge = [[] for _ in range(numCourses)]
        answer = []
        q = deque()

        for to, fr in prerequisites :
            edge[fr].append(to)
            incoming_edge[to] += 1

        for i in range(numCourses) :
            if incoming_edge[i] == 0 :
                q.append(i)

        while q :
            curr = q.popleft()
            answer.append(curr)

            for to in edge[curr] :
                incoming_edge[to] -= 1
                if incoming_edge[to] == 0 :
                    q.append(to)

        for i in range(numCourses) :
            if incoming_edge[i] != 0 :
                return []

        return answer