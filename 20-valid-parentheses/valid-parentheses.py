class Solution:
    def isValid(self, s: str) -> bool:
        input_stack = ['(', '{', '[']
        stack = []

        for char in s :
            if char in input_stack :
                stack.append(char)

            else :
                if not stack :
                    return False
                    
                curr = stack.pop()
                if curr == '(' :
                    if char != ')' :
                        return False
                
                elif curr == '{' :
                    if char !=  '}' :
                        return False
                
                else :
                    if char != ']' :
                        return False
            
        if stack :
            return False
        else :
            return True