class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        start = strs[0]
        n = len(start)

        for s in strs[1:] :
            while n != 0 :
                if s[:n] == start[:n] : 
                    break
                else :
                    n -= 1
        
        return start[:n]