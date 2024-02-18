class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        ans = [0, 0]
        
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]

# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         s_prime = '#' + '#'.join(s) + '#'
#         n = len(s_prime)
#         palindrome_radii = [0] * n
#         center = radius = 0
        
#         for i in range(n):
#             mirror = 2 * center - i

#             if i < radius:
#                 palindrome_radii[i] = min(radius - i, palindrome_radii[mirror])

#             while (i + 1 + palindrome_radii[i] < n and 
#                    i - 1 - palindrome_radii[i] >= 0 and
#                    s_prime[i + 1 + palindrome_radii[i]] == s_prime[i - 1 - palindrome_radii[i]]):
#                 palindrome_radii[i] += 1

#             if i + palindrome_radii[i] > radius:
#                 center = i
#                 radius = i + palindrome_radii[i]

#         max_length = max(palindrome_radii)
#         center_index = palindrome_radii.index(max_length)
#         start_index = (center_index - max_length) // 2
#         longest_palindrome = s[start_index: start_index + max_length]

#         return longest_palindrome