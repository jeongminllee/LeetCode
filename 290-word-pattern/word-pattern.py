class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s) :
            return False
            
        c2word = {}
        word2c = {}

        for i in range(len(pattern)) :
            if pattern[i] not in c2word :
                c2word[pattern[i]] = s[i]
            else :
                if c2word[pattern[i]] != s[i] :
                    return False
        
        for i in range(len(s)) :
            if s[i] not in word2c :
                word2c[s[i]] = pattern[i]
            else :
                if word2c[s[i]] != pattern[i] :
                    return False

        return True