def calculate(m, n, sx, sy, ax, ay):
    ans = []

    # 상
    if not (sx == ax and sy < ay):
        dist = (sx - ax) ** 2 + (2 * n - ay - sy) ** 2
        ans.append(dist)
    # 하
    if not (sx == ax and sy > ay):
        dist = (sx - ax) ** 2 + (sy + ay) ** 2
        ans.append(dist)
    # 좌
    if not (sy == ay and sx > ax):
        dist = (sx + ax) ** 2 + (sy - ay) ** 2
        ans.append(dist)
    # 우
    if not (sy == ay and sx < ax):
        dist = (2 * m - ax - sx) ** 2 + (sy - ay) ** 2
        ans.append(dist)

    return min(ans)


def solution(m, n, startX, startY, balls):
    answer = []

    for ball in balls:
        answer.append(calculate(m, n, startX, startY, ball[0], ball[1]))

    return answer

