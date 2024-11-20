from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board, num):
    puzzle_coord = []
    visited = [[False] * len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if not visited[i][j] and board[i][j] == num:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                cand = [(i, j)]

                while q:
                    x, y = q.popleft()
                    for _ in range(4):
                        nx = x + dx[_]
                        ny = y + dy[_]
                        if nx < 0 or nx > len(board) - 1 or ny < 0 or ny > len(board[0]) - 1:
                            continue
                        if board[nx][ny] == num and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            cand.append((nx, ny))

                puzzle_coord.append(cand)

    return puzzle_coord


def make_array(coord):
    x, y = zip(*coord)
    r, c = max(x) - min(x) + 1, max(y) - min(y) + 1
    array = [[0] * c for _ in range(r)]

    for i, j in coord:
        i, j = i - min(x), j - min(y)
        array[i][j] = 1

    return array


def rotate(puzzle):
    rotated = [[0] * len(puzzle) for _ in range(len(puzzle[0]))]
    cnt = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 1:
                cnt += 1
            rotated[j][len(puzzle) - 1 - i] = puzzle[i][j]

    return rotated, cnt


def solution(game_board, table):
    answer = 0

    empty_blocks = bfs(game_board, 0)
    puzzles = bfs(table, 1)

    for block in empty_blocks:
        filled = False
        array = make_array(block)

        for puzzle_original in puzzles:
            if filled:
                break

            puzzle = make_array(puzzle_original)

            for i in range(4):
                puzzle, cnt = rotate(puzzle)

                if array == puzzle:
                    answer += cnt
                    puzzles.remove(puzzle_original)
                    filled = True
                    break

    return answer

