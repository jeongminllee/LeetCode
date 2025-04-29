class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens :
            if t == '+' :
                stack.append(stack.pop() + stack.pop())
            elif t == '-' :
                second = stack.pop()
                first = stack.pop()

                stack.append(first - second)
            elif t == '*' :
                stack.append(stack.pop() * stack.pop())
            elif t == '/' :
                second = stack.pop()
                first = stack.pop()

                stack.append(int(first/second))
            else :
                stack.append(int(t))
        '''
        for t in tokens :
            if t in ["+", "-", "*", "/"] :
                second = stack.pop()
                first = stack.pop()

                if t == '+' :
                    stack.append(first + second)
                elif t == '-' :
                    stack.append(first - second)
                elif t == '*' :
                    stack.append(first * second)
                elif t == '/' :
                    stack.append(int(first/second))
            else :
                stack.append(int(t))
        '''
        return stack[0]