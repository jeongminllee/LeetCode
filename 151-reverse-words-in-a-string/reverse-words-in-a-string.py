class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        lst = lst[::-1]
        res = ''

        for st in lst :
            res += st
            res += ' '
        
        return res[:-1]