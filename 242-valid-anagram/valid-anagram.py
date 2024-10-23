class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nums = []
        numt = []

        for s_ in s :
            nums.append(ord(s_))
        nums.sort()
        
        for t_ in t :
            numt.append(ord(t_))
        numt.sort()

        return nums == numt