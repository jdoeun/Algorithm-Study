def solution(k, ranges):
    answer = []
    sequence = []
    sequence.append(k)

    while k != 1:
        if k % 2 == 1:
            k = k * 3 + 1
        else:
            k //= 2
        sequence.append(k)

    tmp = []

    for x, y in enumerate(sequence):
        tmp.append((x, y))

    areas = []

    for i in range(len(tmp) - 1):
        x1, y1 = tmp[i]
        x2, y2 = tmp[i + 1]
        area = min(y1, y2) * (x2 - x1) + 0.5 * abs(y1 - y2) * (x2 - x1)
        areas.append(area)

    n = len(sequence) - 1

    for a, b in ranges:
        start, end = a, n + b
        if start > end:
            answer.append(-1.0)
            continue
        if start == end:
            answer.append(0.0)
            continue
        answer.append(sum(areas[start:end]))

    return answer
