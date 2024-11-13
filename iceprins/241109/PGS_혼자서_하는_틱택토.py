def check_winning(board):
    win_O, win_X = 0, 0

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "O":
            win_O += 1
        elif board[0][0] == "X":
            win_X += 1

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "O":
            win_O += 1
        elif board[0][2] == "X":
            win_X += 1

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "O":
                win_O += 1
            elif board[i][0] == "X":
                win_X += 1
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "O":
                win_O += 1
            elif board[0][i] == "X":
                win_X += 1

    return [win_O, win_X]


def solution(board):
    num_O, num_X = 0, 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                num_O += 1
            elif board[i][j] == "X":
                num_X += 1
    if num_O == 0 and num_X == 0:
        return 1

    win_O, win_X = check_winning(board)

    # 빙고가 두 개 이상 있는 경우
    if win_O and win_X:
        return 0

    # 선공과 후공이 같은 횟수로 표시한 경우
    if num_O == num_X:
        # 선공이 이겼다면 불가능한 경우에 해당 -> 선공이 이겼다면 후공이 하나 덜 표시했어야 함
        if win_O >= 1:
            return 0
        # 후공이 이겼다면 가능한 경우에 해당
        else:
            return 1

    # 선공이 후공보다 하나 더 표시한 경우
    if num_O == (num_X + 1):
        # 선공은 지고 후공이 이겼다면 불가능한 경우에 해당
        if (win_O == 0 and win_X >= 1):
            return 0
        # 선공이 이겼거나 후공이 진 경우는 가능한 경우에 해당
        else:
            return 1

    # 그 외에는 모두 불가능한 경우에 해당
    return 0

