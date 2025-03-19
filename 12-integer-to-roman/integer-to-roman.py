class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        while num > 0 :
            if num >= 1000 :
                res += 'M'
                num -= 1000
            elif 900 <= num < 1000 :  # < 1000 은 생략해도 될거 같은데 변수 제거 용으로 남겨둠
                res += 'CM'
                num -= 900
            elif 500 <= num < 900 :
                res += 'D'
                num -= 500
            elif 400 <= num < 500 :
                res += 'CD'
                num -= 400
            elif 100 <= num < 400 :
                res += 'C'
                num -= 100
            elif 90 <= num < 100 :
                res += 'XC'
                num -= 90
            elif 50 <= num < 90 :
                res += 'L'
                num -= 50
            elif 40 <= num < 50 :
                res += 'XL'
                num -= 40
            elif 10 <= num < 40 :
                res += 'X'
                num -= 10
            elif 9 <= num < 10 :
                res += 'IX'
                num -= 9
            elif 5 <= num < 9 :
                res += 'V'
                num -= 5
            elif 4 <= num < 5 :
                res += 'IV'
                num -= 4
            elif 1 <= num < 4 :
                res += 'I'
                num -= 1
        return res