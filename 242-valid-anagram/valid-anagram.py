# 문자를 재조합했을때 두 문자가 같아지면 t, 아니면 f
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        
        if s == t :
            return True
        else :
            return False