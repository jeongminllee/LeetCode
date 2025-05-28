class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = right = 0

        for i in range(len(s)) :
            odd = self.palindrome(s, i, i)
            even = self.palindrome(s, i, i + 1)
            max_length = max(odd, even)

            if max_length > right - left :
                left = i - (max_length - 1) // 2
                right = i + max_length // 2

        return s[left:right+1]

    def palindrome(self, s, left, right) :
        while 0 <= left and right < len(s) and s[left] == s[right] :
            left -= 1
            right += 1
        return (right - 1) - (left + 1) + 1