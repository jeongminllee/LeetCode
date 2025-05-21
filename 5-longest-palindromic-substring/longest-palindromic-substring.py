class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = right = 0

        for i in range(len(s)) :
            odd = self.expand_around_center(s, i, i)
            even = self.expand_around_center(s, i, i + 1)
            max_length = max(odd, even)

            if max_length > right - left :
                left = i - (max_length - 1) // 2
                right = i + max_length // 2

        return s[left:right+1]

    def expand_around_center(self, s: str, left: int, right: int) -> int :
        while 0 <= left and right < len(s) and s[left] == s[right] :
            left -= 1
            right += 1
        
        return right - left - 1