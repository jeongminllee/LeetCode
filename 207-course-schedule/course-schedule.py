class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = [0] * numCourses

        pre = defaultdict(list)

        for course, p in prerequisites :
            pre[course].append(p)

        def dfs(node) :
            visited[node] = 1

            for neighbor in pre[node] :
                if visited[neighbor] == 0 :
                    if dfs(neighbor) :
                        return True

                elif visited[neighbor] == 1 :
                    return True


            visited[node] = 2
            return False

        for node in range(numCourses) :
            if visited[node] == 0 :
                if dfs(node) :
                    return False

        return True