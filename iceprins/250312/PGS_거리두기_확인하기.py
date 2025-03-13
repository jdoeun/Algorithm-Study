from itertools import combinations


def get_manhattan(spot1, spot2):
    return abs(spot1[0] - spot2[0]) + abs(spot1[1] - spot2[1])


def solution(places):
    answer = []

    for room in places:
        seats = []
        for i in range(5):
            for j in range(5):
                if room[i][j] == "P":
                    seats.append((i, j))
        combs = list(combinations(seats, 2))
        tmp = 1
        for comb in combs:
            p1, p2 = comb
            d = get_manhattan(p1, p2)
            if d > 2:
                continue
            if d == 1:
                tmp = 0
                break
            if d == 2:
                if p1[0] == p2[0] and room[p1[0]][(p1[1] + p2[1]) // 2] == "X":
                    continue
                if p1[1] == p2[1] and room[(p1[0] + p2[0]) // 2][p1[1]] == "X":
                    continue
                if p1[0] > p2[0] and p2[0] + 1 == p1[0] and p2[1] + 1 == p1[1] and room[p2[0]][p1[1]] == "X" and \
                        room[p1[0]][p2[1]] == "X":
                    continue
                if p1[0] > p2[0] and p2[0] + 1 == p1[0] and p2[1] - 1 == p1[1] and room[p2[0]][p1[1]] == "X" and \
                        room[p1[0]][p2[1]] == "X":
                    continue
                if p1[0] < p2[0] and p1[0] + 1 == p2[0] and p1[1] + 1 == p2[1] and room[p1[0]][p2[1]] == "X" and \
                        room[p2[0]][p1[1]] == "X":
                    continue
                if p1[0] < p2[0] and p1[0] + 1 == p2[0] and p1[1] - 1 == p2[1] and room[p1[0]][p2[1]] == "X" and \
                        room[p2[0]][p1[1]] == "X":
                    continue
                tmp = 0
                break

        answer.append(tmp)

    return answer

