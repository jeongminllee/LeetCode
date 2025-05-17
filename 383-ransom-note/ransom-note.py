class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashTable = {}
        for maga in magazine :
            hashTable[maga] = 1 + hashTable.get(maga, 0)
            
        for ransom in ransomNote :
            if ransom not in hashTable or hashTable[ransom] <= 0 :
                return False

            hashTable[ransom] -= 1
        
        return True