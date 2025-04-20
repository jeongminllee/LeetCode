class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0 :
            r = n % 2
            res += r
            n //= 2
        
        return res