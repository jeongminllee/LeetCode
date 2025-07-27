class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wlen = len(words[0])
        total = len(words) * wlen

        def frequency_map(word_list) :
            freq = {}
            for ch in word_list :
                freq[ch] = freq.get(ch, 0) + 1
            return freq

        main = frequency_map(words) 
        res = []

        for start in range(len(s) - total + 1) :
            s_parts = [s[i:i+wlen] for i in range(start, start + total, wlen)]
            if frequency_map(s_parts) == main :
                res.append(start)

        return res