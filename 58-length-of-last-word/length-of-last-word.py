class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_sp = s.split()
        return len(s_sp[-1])