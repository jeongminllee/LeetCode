class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        return self.mywordBreak(s, 0, n, wordDict, dp)

    def mywordBreak(self, s: str, fr: int, length: int, wordDict: List[str], dp: List[bool]):
        if fr == length :
            return True

        for word in wordDict :
            if fr + len(word) <= length and dp[fr + len(word)] == False and s[fr:fr + len(word)] == word :
                dp[fr + len(word)] = True
                if self.mywordBreak(s, fr+len(word), length, wordDict, dp) :
                    return True

        return False