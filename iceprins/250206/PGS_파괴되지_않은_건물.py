def solution(board, skill):
    answer = 0

    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for t, r1, c1, r2, c2, intensity in skill:
        if t == 1:
            tmp[r1][c1] -= intensity
            tmp[r1][c2 + 1] += intensity
            tmp[r2 + 1][c1] += intensity
            tmp[r2 + 1][c2 + 1] -= intensity
        else:
            tmp[r1][c1] += intensity
            tmp[r1][c2 + 1] -= intensity
            tmp[r2 + 1][c1] -= intensity
            tmp[r2 + 1][c2 + 1] += intensity

    for i in range(len(tmp) - 1):
        for j in range(len(tmp[0]) - 1):
            tmp[i][j + 1] += tmp[i][j]

    for j in range(len(tmp[0]) - 1):
        for i in range(len(tmp) - 1):
            tmp[i + 1][j] += tmp[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += tmp[i][j]
            if board[i][j] >= 1:
                answer += 1

    return answer

