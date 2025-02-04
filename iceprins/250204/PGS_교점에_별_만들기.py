from itertools import combinations


def get_points(eq1, eq2):
    denominator = (eq1[0] * eq2[1] - eq1[1] * eq2[0])
    if denominator == 0:
        return

    x = (eq1[1] * eq2[2] - eq1[2] * eq2[1]) / denominator
    y = (eq1[2] * eq2[0] - eq1[0] * eq2[2]) / denominator

    if x == int(x) and y == int(y):
        return [int(x), int(y)]


def solution(line):
    points = []

    for eq1, eq2 in combinations(line, 2):
        point = get_points(eq1, eq2)
        if point:
            points.append(point)

    w1, w2 = min(points, key=lambda x: x[0])[0], max(points, key=lambda x: x[0])[0] + 1
    h1, h2 = min(points, key=lambda x: x[1])[1], max(points, key=lambda x: x[1])[1] + 1

    answer = [["."] * (w2 - w1) for _ in range(h2 - h1)]

    for x, y in points:
        answer[y - h1][x - w1] = "*"

    answer.reverse()

    return [''.join(a) for a in answer]

