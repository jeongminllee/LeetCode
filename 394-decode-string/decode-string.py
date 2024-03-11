class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""
        for c in s :
            # 숫자 파싱 : 입력된 문자열을 순회하며 숫자를 만나면, 이전에 파싱된 숫자에 10을 곱하고 현재 숫잘르 더해줌으로써,
            # 여러 자리 숫자도 올바르게 파싱할 수 있습니다.
            if c.isdigit() :
                curr_num = curr_num * 10 + int(c)
            # [ 처리 : [ 를 만나면 지금까지 파싱된 숫자와 문자열을 스택에 저장하고, 숫자와 문자열 변수를 초기화합니다.
            # 이는 새로운 문자열의반복을 처리하기 위함입니다.
            elif c == '[' :
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            # ] 처리 : ] 를 만나면 스택에 이전 문자열과 반복 횟수를 꺼내고, 현재 문자열을 반복 횟수만큼 반복한 뒤,
            # 이전 문자열에 이어 붙입니다. 이 과정을 괄호 안의 문자열 반복을 처리합니다.
            elif c == ']' :
                prev_str, prev_num = stack.pop()
                curr_str = prev_str + curr_str * prev_num
            # 문자 처리 : 알파벳 문자를 만나면 현재 문자열에 추가합니다.
            # 이는 스택에 저장되어 있던 문자열에 추가되거나, 새로운 문자열을 구상하기 위함입니다.
            else :
                curr_str += c
        return curr_str