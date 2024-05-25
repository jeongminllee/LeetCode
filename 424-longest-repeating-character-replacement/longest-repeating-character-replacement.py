class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxlen, largestcnt = 0, 0
        arr =  Counter()
        for idx in range(len(s)) :
            arr[s[idx]] += 1
            largestcnt = max(largestcnt, arr[s[idx]])
            if maxlen - largestcnt >= k :
                arr[s[idx - maxlen]] -= 1
            else :
                maxlen += 1
        return maxlen