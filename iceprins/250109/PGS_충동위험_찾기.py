from collections import Counter


def solution(points, routes):
    def bfs(route):
        idx = 0
        record = []
        for i in range(len(route) - 1):
            sx, sy = spots[route[i] - 1]
            ex, ey = spots[route[i + 1] - 1]

            while sx != ex:
                record.append((sx, sy, idx))
                if sx < ex:
                    sx += 1
                else:
                    sx -= 1
                idx += 1

            while sy != ey:
                record.append((sx, sy, idx))
                if sy < ey:
                    sy += 1
                else:
                    sy -= 1
                idx += 1

        record.append((sx, sy, idx))
        return record

    spots = [i for i in points]
    second = []

    for route in routes:
        second.extend(bfs(route))

    cnt = 0
    temp = Counter(second)
    for i in temp.values():
        if i >= 2:
            cnt += 1

    return cnt

