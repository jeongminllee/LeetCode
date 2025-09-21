class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
            
        dct = {}
        for s_ in s :
            dct[s_] = dct.get(s_, 0) + 1

        for t_ in t :
            if t_ not in dct or dct[t_] == 0 :
                return False
            dct[t_] -= 1
        
        return True