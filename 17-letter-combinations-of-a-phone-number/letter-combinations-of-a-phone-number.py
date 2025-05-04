class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '' :
            return []

        numbers_to_letter = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        
        stack = []

        def backtrack(idx, res) :
            if idx == len(digits) :
                stack.append(res[:])
                return

            for letter in numbers_to_letter[digits[idx]] :
                backtrack(idx + 1, res + letter)

        backtrack(0, '')
        return stack