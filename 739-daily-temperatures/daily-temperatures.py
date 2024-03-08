class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        if n == 1 :
            return [0]
        
        ans = [0] * n
        stack = [n - 1]

        for i in range(n - 2, -1, -1) :
            while stack and t[i] >= t[stack[-1]] :
                stack.pop()
            if stack :
                ans[i] = stack[-1] - i
            
            stack.append(i)
            
        return ans