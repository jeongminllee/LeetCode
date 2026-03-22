class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in range(len(s)) :
            if s[i] not in s_map :
                s_map[s[i]] = t[i]

            else :
                if s_map[s[i]] == t[i] :
                    continue
                else :
                    return False

            if t[i] not in t_map :
                t_map[t[i]] = s[i]

            else :
                if t_map[t[i]] == s[i] :
                    continue
                else :
                    return False
        
        return True