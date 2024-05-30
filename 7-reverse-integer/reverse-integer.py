class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        flag = True
        if s[0] == "-" :
            s = s[1:]
            flag = False

        s = s[::-1]

        if flag :
            s = int(s)
        else :
            s = -int(s)

        if -(2 ** 31) <= s < (2 ** 31) :
            return s
        else :
            return 0