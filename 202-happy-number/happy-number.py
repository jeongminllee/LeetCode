class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 :
            if n in visited :
                return False
            visited.add(n)
            n = sum((int(num)%10)**2 for num in str(n))
            
        return True