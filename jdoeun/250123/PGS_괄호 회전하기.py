def solution(s):
    answer = 0
    s = list(s)

    for _ in range(len(s)):  # 문자열을 왼쪽으로 한 칸씩 회전
        stack = []
        for i in range(len(s)):  # 현재 회전된 문자열에 대해 올바른 괄호 문자열인지 확인
            if len(stack) > 0:
                if stack[-1] == '[' and s[i] == ']':
                    stack.pop()
                elif stack[-1] == '{' and s[i] == '}':
                    stack.pop()
                elif stack[-1] == '(' and s[i] == ')':
                    stack.pop()
                else:
                    stack.append(s[i])  # 현재 문자가 스택의 마지막 괄호와 짝이 맞지 않아, 쌓아야 하는 경우
            else:
                stack.append(s[i])  # 스택이 비어 있어서 괄호를 쌓아야 하는 경우

        if len(stack) == 0:
            answer += 1
        s.append(s.pop(0))  # 문자열 회전

    return answer