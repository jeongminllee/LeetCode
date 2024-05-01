class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word :
            return word
        
        for i in range(len(word)) :
            if word[i] == ch :
                lst = word[:i+1]
                break
        
        return lst[::-1] + word[i+1:]