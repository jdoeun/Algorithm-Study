def solution(s):
    st = []
    for char in s:
        if len(st) == 0:
            st.append(char)
        elif st[-1] == char:
            st.pop()
        else:
            st.append(char)

    if len(st) == 0:
        return 1

    return 0

