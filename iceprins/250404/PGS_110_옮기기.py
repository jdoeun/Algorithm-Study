def solution(s):
    answer = []

    for n in s:
        cnt, idx, st = 0, 0, ""
        while idx < len(n):
            if n[idx] == "0" and st[-2:] == "11":
                st = st[:-2]
                cnt += 1
            else:
                st += n[idx]
            idx += 1

        idx = st.find("111")
        if idx == -1:
            idx = st.rfind("0")
            st = st[:idx + 1] + "110" * cnt + st[idx + 1:]
        else:
            st = st[:idx] + "110" * cnt + st[idx:]
        answer.append(st)

    return answer

