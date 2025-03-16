class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)

        nums = a + b
        res = bin(nums)[2:]
        return res