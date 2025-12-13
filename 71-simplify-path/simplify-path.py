class Solution:
    def simplifyPath(self, path: str) -> str:
        path_sp = path.split("/")
        stack = []

        for p in path_sp :
            if p == "" or p == ".":
                continue

            if p == ".." :
                if stack :
                    stack.pop()
                continue
            
            stack.append(p)

        return "/" + "/".join(stack)