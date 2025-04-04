def solution(dirs):
    answer = 0
    x, y = 0, 0
    record = []

    for d in dirs:
        if d == "U":
            if y == 5:
                continue
            if (x, y, x, y + 1) not in record and (x, y + 1, x, y) not in record:
                record.append((x, y, x, y + 1))
                answer += 1
            y += 1
        elif d == "D":
            if y == -5:
                continue
            if (x, y, x, y - 1) not in record and (x, y - 1, x, y) not in record:
                record.append((x, y, x, y - 1))
                answer += 1
            y -= 1
        elif d == "R":
            if x == 5:
                continue
            if (x, y, x + 1, y) not in record and (x + 1, y, x, y) not in record:
                record.append((x, y, x + 1, y))
                answer += 1
            x += 1
        else:
            if x == -5:
                continue
            if (x, y, x - 1, y) not in record and (x - 1, y, x, y) not in record:
                record.append((x, y, x - 1, y))
                answer += 1
            x -= 1

    return answer

