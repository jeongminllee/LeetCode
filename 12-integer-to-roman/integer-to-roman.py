class Solution:
    def intToRoman(self, n: int) -> str:
        res = ''
        while n > 0 :
            if n >= 1000 :
                res += 'M'
                n -= 1000
            elif 900 <= n < 1000 :  # < 1000 은 생략해도 될거 같은데 변수 제거 용으로 남겨둠
                res += 'CM'
                n -= 900
            elif 500 <= n < 900 :
                res += 'D'
                n -= 500
            elif 400 <= n < 500 :
                res += 'CD'
                n -= 400
            elif 100 <= n < 400 :
                res += 'C'
                n -= 100
            elif 90 <= n < 100 :
                res += 'XC'
                n -= 90
            elif 50 <= n < 90 :
                res += 'L'
                n -= 50
            elif 40 <= n < 50 :
                res += 'XL'
                n -= 40
            elif 10 <= n < 40 :
                res += 'X'
                n -= 10
            elif 9 <= n < 10 :
                res += 'IX'
                n -= 9
            elif 5 <= n < 9 :
                res += 'V'
                n -= 5
            elif 4 <= n < 5 :
                res += 'IV'
                n -= 4
            elif 1 <= n < 4 :
                res += 'I'
                n -= 1
        return res