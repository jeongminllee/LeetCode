class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for character in s :
            if character.isalnum() :
                res += character.lower()
        
        n = len(res)
        left, right = 0, n-1

        while left <= right :
            if res[left] == res[right] :
                left += 1
                right -= 1
            else :
                return False

        return True