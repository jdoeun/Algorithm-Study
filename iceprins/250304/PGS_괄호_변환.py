def division(s):
    left, right = 0, 0
    for i in range(len(s)):
        if s[i] == "(":
            left += 1
        elif s[i] == ")":
            right += 1
        if left == right:
            return [s[:i + 1], s[i + 1:]]


def is_correct(s):
    st = []
    for x in s:
        if x == ")":
            if not st:
                return False
            if st[-1] == "(":
                st.pop()
        elif x == "(":
            st.append(x)

    if not st:
        return True

    return False


def solution(p):
    answer = ''
    u, v = "", ""

    if p == "":
        return ""

    u, v = division(p)

    if is_correct(u):
        return u + solution(v)

    answer += "("
    answer += solution(v)
    answer += ")"

    for x in u[1:len(u) - 1]:
        if x == "(":
            answer += ")"
        else:
            answer += "("

    return answer

