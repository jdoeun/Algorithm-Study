from collections import deque


def check(s):
    st = []
    for char in s:
        if char == "(" or char == "[" or char == "{":
            st.append(char)
        elif char == ")":
            if not st:
                return False
            if st[-1] != "(":
                return False
            st.pop()
        elif char == "]":
            if not st:
                return False
            if st[-1] != "[":
                return False
            st.pop()
        elif char == "}":
            if not st:
                return False
            if st[-1] != "{":
                return False
            st.pop()

    return len(st) == 0


def solution(s):
    answer = 0

    q = deque(s)

    for _ in range(len(q)):
        q.rotate()
        result = check(q)
        if result:
            answer += 1

    return answer

