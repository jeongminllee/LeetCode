class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        return self.mywordbreak(s, 0, len(s), wordDict, dp)

    def mywordbreak(self, s:str, fr: int, length: int, wordDict: List[str], dp: List[bool]) :
        if fr == length :
            return True

        for word in wordDict :
            nxt = fr + len(word)
            if nxt <= length and dp[nxt] == False and s[fr : nxt] == word :
                dp[fr + len(word)] = True
                if self.mywordbreak(s, nxt, length, wordDict, dp) :
                    return True
                
        return False