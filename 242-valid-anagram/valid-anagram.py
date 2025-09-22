class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        
        words = {}

        for char in s :
            words[char] = words.get(char, 0) + 1
        
        for char in t :
            if char not in words or words[char] == 0 :
                return False
            words[char] -= 1
        
        return True