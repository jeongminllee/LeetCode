class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        roman = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        roman_num = (1, 5, 10, 50, 100, 500, 1000)

        for a, b in zip(s, s[1:]) :
            if roman_num[roman.index(a)] < roman_num[roman.index(b)] :
                ans -= roman_num[roman.index(a)]

            else :
                ans += roman_num[roman.index(a)]
                
        return ans + roman_num[roman.index(s[-1])]