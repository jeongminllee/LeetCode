class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct_s = {}
        dct_t = {}
        
        for i in range(len(s)) :
            if s[i] not in dct_s.keys() :
                dct_s[s[i]] = t[i]

            else :
                if dct_s[s[i]] != t[i] :
                    return False

        for i in range(len(t)) :
            if t[i] not in dct_t.keys() :
                dct_t[t[i]] = s[i]

            else :
                if dct_t[t[i]] != s[i] :
                    return False
        
        return True