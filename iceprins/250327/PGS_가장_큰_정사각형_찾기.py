def solution(board):
    r, c = len(board), len(board[0])

    dp = [[0] * c for _ in range(r)]
    dp[0] = board[0]

    for i in range(1, r):
        dp[i][0] = board[i][0]

    for i in range(1, r):
        for j in range(1, c):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    answer = 0

    for i in range(r):
        tmp = max(dp[i])
        answer = max(answer, tmp)

    return answer ** 2

