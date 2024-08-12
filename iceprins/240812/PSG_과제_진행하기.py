def solution(plans):
    answer = []
    saved = []

    for i in range(len(plans)):
        hour, minute = map(int, plans[i][1].split(":"))
        plans[i][1] = hour * 60 + minute
        plans[i][2] = int(plans[i][2])

    plans.sort(key=lambda x: x[1])

    for i in range(len(plans)):
        if i == len(plans) - 1:
            saved.append(plans[i])
            break

        n, s, p = plans[i]
        nn, ns, np = plans[i + 1]

        if s + p <= ns:
            answer.append(n)
            rest = ns - (s + p)

            while rest != 0 and saved:
                sn, ss, sp = saved.pop()
                if rest >= sp:
                    answer.append(sn)
                    rest -= sp
                else:
                    saved.append([sn, ss, sp - rest])
                    rest = 0

        else:
            plans[i][2] = p - (ns - s)
            saved.append(plans[i])

    while saved:
        sn, ss, sp = saved.pop()
        answer.append(sn)

    return answer
