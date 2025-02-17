def solution(s):
    stack = []

    for char in s:
        # 스택이 비어 있지 않고, 가장 마지막 문자가 현재 문자와 같음
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return 1 if not stack else 0