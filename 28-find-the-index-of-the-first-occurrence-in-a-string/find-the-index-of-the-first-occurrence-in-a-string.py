class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if n < m :
            return -1

        if needle not in haystack :
            return -1

        for left in range(n) :
            if haystack[left:left+m] == needle :
                return left

        return -1