class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 :
            return True

        if len(s) > len(t) :
            return False

        if len(s) == len(t) and s != t :
            return False
        elif s == t :
            return True


        s_idx = t_idx = 0

        while s_idx != len(s) and t_idx != len(t) :
            if s[s_idx] == t[t_idx] :
                s_idx += 1

            t_idx += 1

        if s_idx == len(s) :
            return True
        else :
            return False