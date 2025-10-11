class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman = [
            ['I',1],
            ['IV', 4],
            ['V', 5],
            ['IX', 9],
            ['X',10],
            ['XL', 40],
            ['L',50],
            ['XC', 90],
            ['C',100],
            ['CD', 400],
            ['D',500],
            ['CM', 900],
            ['M',1000]
        ]

        # 초기값
        cnt = 0
        res = ''

        for roman, inti in reversed(int_to_roman) :
            cnt = num // inti
            res += roman * cnt
            num %= inti
        
        return res