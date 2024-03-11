class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""
        for c in s :
            if c.isdigit() :
                curr_num = curr_num * 10 + int(c)
            elif c == '[' :
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif c == ']' :
                prev_str, prev_num = stack.pop()
                curr_str = prev_str + curr_str * prev_num
            else :
                curr_str += c
        return curr_str