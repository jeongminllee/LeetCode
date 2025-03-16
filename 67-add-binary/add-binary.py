class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = decimal_b = 0
        res = []
        ans = ''
        
        for i in range(len(a)) :
            if a[i] == '1' :
                decimal_a += 1 << (len(a) - i - 1)

        for i in range(len(b)) :
            if b[i] == '1' :
                decimal_b += 1 << (len(b) - i - 1)

        # print('decimal_a', decimal_a)
        # print('decimal_b', decimal_b)

        nums = decimal_a + decimal_b
        # res = bin(nums)[2:]

        while nums != 0 :
            residue = nums % 2
            res.append(str(residue))
            nums //= 2
        ans = ''.join(res[::-1])
        return ans if ans != '' else '0'