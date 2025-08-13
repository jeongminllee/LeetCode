class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = defaultdict(list)

        for word in strs :
            sorted_word = ''.join(sorted(word))
            group_anagram[sorted_word].append(word)


        return list(group_anagram.values())