class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        c2word = {}
        word2c = {}

        s = s.split()

        if len(pattern) != len(s) :
            return False

        for i in range(len(pattern)) :
            char = pattern[i]
            if char not in c2word :
                c2word[char] = s[i]
            else :
                if c2word[char] == s[i] :
                    continue
                else :
                    return False
        
        for i in range(len(s)) :
            word = s[i]
            if word not in word2c :
                word2c[word] = pattern[i]
            else :
                if word2c[word] == pattern[i] :
                    continue
                else :
                    return False
        
        return True