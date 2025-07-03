class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ['a']
        while len(word) < k :
            word += [chr(ord(c) + 1) for c in word]
        
        return word[k - 1]
