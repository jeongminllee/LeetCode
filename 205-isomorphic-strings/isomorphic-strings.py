class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct_s = {}
        dct_t = {}

        for idx in range(len(s)) :
            if s[idx] not in dct_s.keys() :
                dct_s[s[idx]] = t[idx]

            else :
                if dct_s[s[idx]] != t[idx] :
                    return False

        for idx in range(len(t)) :
            if t[idx] not in dct_t.keys() :
                dct_t[t[idx]] = s[idx]
            else :
                if dct_t[t[idx]] != s[idx] :
                    return False

        return True