from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrom_map = defaultdict(list)

        for word in strs :
            sorted_word = ''.join(sorted(word))
            anagrom_map[sorted_word].append(word)

        return list(anagrom_map.values())