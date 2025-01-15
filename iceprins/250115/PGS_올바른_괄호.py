def solution(s):
    s = list(s)

    st = []

    for x in s:
        if x == ")":
            if not st:
                return False
            if st[-1] == ")":
                return False
            st.pop()
        else:
            st.append(x)

    if st:
        return False
    return True

