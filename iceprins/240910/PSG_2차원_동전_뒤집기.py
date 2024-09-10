def solution(beginning, target):
    r, c = len(beginning), len(beginning[0])
    diff = [[beginning[i][j] ^ target[i][j] for j in range(c)] for i in range(r)]

    cnt_r = 0

    for i in range(1, r):
        if diff[i] != diff[0]:
            cnt_r += 1
            if list(map(lambda x: (x + 1) % 2, diff[i])) != diff[0]:
                return -1

    cnt_c = sum(diff[0])

    return min(cnt_r + cnt_c, (r - cnt_r) + (c - cnt_c))
