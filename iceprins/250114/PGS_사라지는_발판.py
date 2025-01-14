dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def A_turn(ar, ac, br, bc, cnt, board):
    if board[ar][ac] == 0:
        return (1, cnt)
    winner = []
    loser = []
    flag = False
    for i in range(4):
        nr = ar + dr[i]
        nc = ac + dc[i]
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 1:
            flag = True
            tmp = [row[:] for row in board]
            tmp[ar][ac] = 0
            is_win, turn = B_turn(br, bc, nr, nc, cnt + 1, tmp)
            if is_win:
                winner.append(turn)
            else:
                loser.append(turn)
    if flag:
        if winner:
            return (0, min(winner))
        else:
            return (1, max(loser))
    else:
        return (1, cnt)


def B_turn(br, bc, ar, ac, cnt, board):
    if board[br][bc] == 0:
        return (1, cnt)
    winner = []
    loser = []
    flag = False
    for i in range(4):
        nr = br + dr[i]
        nc = bc + dc[i]
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 1:
            flag = True
            tmp = [row[:] for row in board]
            tmp[br][bc] = 0
            is_win, turn = A_turn(ar, ac, nr, nc, cnt + 1, tmp)
            if is_win:
                winner.append(turn)
            else:
                loser.append(turn)
    if flag:
        if winner:
            return (0, min(winner))
        else:
            return (1, max(loser))
    else:
        return (1, cnt)


def solution(board, aloc, bloc):
    ar, ac, br, bc = aloc[0], aloc[1], bloc[0], bloc[1]
    answer = A_turn(ar, ac, br, bc, 0, board)[1]
    return answer

