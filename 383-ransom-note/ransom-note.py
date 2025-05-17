class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine) :
            return False

        hashTable = {}
        for maga in magazine :
            if maga not in hashTable :
                hashTable[maga] = 1
            else :
                hashTable[maga] += 1

        for ransom in ransomNote :
            if ransom not in hashTable or hashTable[ransom] <= 0 :
                return False

            if hashTable[ransom] :
                hashTable[ransom] -= 1
        
        return True